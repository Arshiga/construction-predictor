import logging
import re
from flask import Blueprint, request, jsonify, send_file
from app import db, limiter
from app.models.database import Project, Prediction, Feedback
from app.ml.predictor import CostDelayPredictor
from app.ml.govt_estimator import GovtCostEstimator
from app.services.pdf_generator import pdf_generator
from app.services.cost_optimizer import cost_optimizer
import os

bp = Blueprint('predictions', __name__, url_prefix='/api/predictions')
logger = logging.getLogger(__name__)

# Initialize predictor
MODEL_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'trained_models')
predictor = CostDelayPredictor(model_dir=MODEL_DIR)

# Initialize government estimator
govt_estimator = GovtCostEstimator()

# --- Issue #5 & #6: Input validation helpers ---

VALID_PROJECT_TYPES = {'residential', 'commercial', 'industrial', 'infrastructure'}
VALID_MATERIAL_QUALITY = {'economy', 'standard', 'premium'}
VALID_COMPLEXITY = {'low', 'medium', 'high'}
VALID_WEATHER_RISK = {'low', 'moderate', 'high'}
VALID_SOIL_TYPES = {'normal', 'rocky', 'sandy', 'clayey', 'marshy', 'black_cotton'}
VALID_WATER_TABLE = {'deep', 'moderate', 'shallow'}
VALID_ACCESSIBILITY = {'easy', 'moderate', 'difficult'}
VALID_FOUNDATION = {'isolated', 'combined', 'raft', 'pile'}
VALID_FINISHING = {'basic', 'standard', 'premium', 'luxury'}
VALID_TOPOGRAPHY = {'flat', 'sloped', 'hilly'}

# Regex to sanitize string inputs — only letters, numbers, spaces, commas, periods, hyphens
SAFE_STRING_PATTERN = re.compile(r'^[a-zA-Z0-9\s,.\-()]+$')


def sanitize_string(value, max_length=200):
    """Sanitize and validate string input"""
    if not isinstance(value, str):
        return None
    value = value.strip()[:max_length]
    if not value:
        return None
    if not SAFE_STRING_PATTERN.match(value):
        return None
    return value


def validate_enum(value, allowed_values, field_name):
    """Validate that value is in allowed set"""
    if value not in allowed_values:
        return f"Invalid {field_name}: '{value}'. Must be one of: {', '.join(sorted(allowed_values))}"
    return None


def validate_positive_number(value, field_name, min_val=0, max_val=None):
    """Validate numeric input is positive and within range"""
    try:
        num = float(value)
    except (TypeError, ValueError):
        return f"{field_name} must be a number"
    if num <= min_val:
        return f"{field_name} must be greater than {min_val}"
    if max_val is not None and num > max_val:
        return f"{field_name} must not exceed {max_val}"
    return None


def validate_prediction_input(data):
    """Validate all prediction input fields. Returns list of errors."""
    errors = []

    # Validate required numeric fields
    err = validate_positive_number(data.get('total_area_sqft'), 'total_area_sqft', min_val=0, max_val=10000000)
    if err:
        errors.append(err)

    err = validate_positive_number(data.get('num_workers'), 'num_workers', min_val=0, max_val=50000)
    if err:
        errors.append(err)

    err = validate_positive_number(data.get('planned_duration_days'), 'planned_duration_days', min_val=0, max_val=36500)
    if err:
        errors.append(err)

    # Validate enum fields
    err = validate_enum(data.get('project_type', 'commercial'), VALID_PROJECT_TYPES, 'project_type')
    if err:
        errors.append(err)

    if 'material_quality' in data:
        err = validate_enum(data['material_quality'], VALID_MATERIAL_QUALITY, 'material_quality')
        if err:
            errors.append(err)

    if 'complexity_level' in data:
        err = validate_enum(data['complexity_level'], VALID_COMPLEXITY, 'complexity_level')
        if err:
            errors.append(err)

    if 'weather_risk_zone' in data:
        err = validate_enum(data['weather_risk_zone'], VALID_WEATHER_RISK, 'weather_risk_zone')
        if err:
            errors.append(err)

    if 'soil_type' in data:
        err = validate_enum(data['soil_type'], VALID_SOIL_TYPES, 'soil_type')
        if err:
            errors.append(err)

    if 'water_table_level' in data:
        err = validate_enum(data['water_table_level'], VALID_WATER_TABLE, 'water_table_level')
        if err:
            errors.append(err)

    if 'site_accessibility' in data:
        err = validate_enum(data['site_accessibility'], VALID_ACCESSIBILITY, 'site_accessibility')
        if err:
            errors.append(err)

    if 'foundation_type' in data:
        err = validate_enum(data['foundation_type'], VALID_FOUNDATION, 'foundation_type')
        if err:
            errors.append(err)

    if 'finishing_level' in data:
        err = validate_enum(data['finishing_level'], VALID_FINISHING, 'finishing_level')
        if err:
            errors.append(err)

    if 'site_topography' in data:
        err = validate_enum(data['site_topography'], VALID_TOPOGRAPHY, 'site_topography')
        if err:
            errors.append(err)

    # Validate optional numeric fields
    if 'num_floors' in data:
        err = validate_positive_number(data['num_floors'], 'num_floors', min_val=-1, max_val=200)
        if err:
            errors.append(err)

    if 'contractor_experience_years' in data:
        err = validate_positive_number(data['contractor_experience_years'], 'contractor_experience_years', min_val=-1, max_val=100)
        if err:
            errors.append(err)

    if 'distance_from_city_km' in data:
        err = validate_positive_number(data['distance_from_city_km'], 'distance_from_city_km', min_val=-1, max_val=5000)
        if err:
            errors.append(err)

    # Validate string fields
    if 'location' in data:
        cleaned = sanitize_string(data['location'])
        if data['location'] and not cleaned:
            errors.append("location contains invalid characters")
        else:
            data['location'] = cleaned or 'Unknown'

    return errors


@bp.route('/predict', methods=['POST'])
@limiter.limit("30 per minute")  # Issue #7: Rate limit expensive ML predictions
def make_prediction():
    """Make a cost and delay prediction for a construction project."""
    data = request.get_json()

    if not data:
        return jsonify({'error': 'No data provided'}), 400

    # Validate required fields
    required_fields = ['project_type', 'total_area_sqft', 'num_workers', 'planned_duration_days']
    missing_fields = [f for f in required_fields if f not in data]
    if missing_fields:
        return jsonify({'error': f'Missing required fields: {missing_fields}'}), 400

    # Set defaults for optional fields
    data.setdefault('location', 'Unknown')
    data.setdefault('num_floors', 1)
    data.setdefault('material_quality', 'standard')
    data.setdefault('complexity_level', 'medium')
    data.setdefault('has_basement', False)
    data.setdefault('weather_risk_zone', 'moderate')
    data.setdefault('contractor_experience_years', 5)
    data.setdefault('soil_type', 'normal')
    data.setdefault('water_table_level', 'deep')
    data.setdefault('distance_from_city_km', 5)
    data.setdefault('site_accessibility', 'easy')
    data.setdefault('floor_height_ft', 10)
    data.setdefault('foundation_type', 'isolated')
    data.setdefault('num_bathrooms', 2)
    data.setdefault('electrical_load_kw', 10)
    data.setdefault('finishing_level', 'standard')
    data.setdefault('site_topography', 'flat')

    # Issue #5 & #6: Validate inputs
    validation_errors = validate_prediction_input(data)
    if validation_errors:
        return jsonify({'error': 'Validation failed', 'details': validation_errors}), 400

    # Make prediction
    try:
        result = predictor.predict(data)
    except Exception as e:
        logger.error(f"Prediction failed: {e}")
        return jsonify({'error': 'Prediction failed. Please check your inputs.'}), 500

    # Save prediction to database
    prediction = Prediction(
        project_id=data.get('project_id'),
        input_data=data,
        predicted_cost=result['predicted_cost'],
        predicted_delay_days=result['predicted_delay_days'],
        delay_probability=result['delay_probability'],
        risk_score=result['risk_score'],
        cost_lower_bound=result['cost_lower_bound'],
        cost_upper_bound=result['cost_upper_bound'],
        delay_lower_bound=result['delay_lower_bound'],
        delay_upper_bound=result['delay_upper_bound'],
        risk_factors=result['risk_factors']
    )

    db.session.add(prediction)
    db.session.commit()

    result['prediction_id'] = prediction.id
    logger.info(f"Prediction {prediction.id} created for project_type={data['project_type']}")
    return jsonify(result), 200


@bp.route('/history', methods=['GET'])
def get_prediction_history():
    """Get all prediction history"""
    predictions = Prediction.query.order_by(Prediction.created_at.desc()).limit(100).all()
    return jsonify([p.to_dict() for p in predictions]), 200


@bp.route('/<int:prediction_id>', methods=['GET'])
def get_prediction(prediction_id):
    """Get a specific prediction by ID"""
    prediction = Prediction.query.get_or_404(prediction_id)
    return jsonify(prediction.to_dict()), 200


@bp.route('/quick-estimate', methods=['POST'])
@limiter.limit("60 per minute")
def quick_estimate():
    """Get a quick estimate without saving to database."""
    data = request.get_json()

    if not data:
        return jsonify({'error': 'No data provided'}), 400

    # Set defaults
    data.setdefault('project_type', 'commercial')
    data.setdefault('location', 'Unknown')
    data.setdefault('total_area_sqft', 10000)
    data.setdefault('num_floors', 1)
    data.setdefault('num_workers', 20)
    data.setdefault('planned_duration_days', 180)
    data.setdefault('material_quality', 'standard')
    data.setdefault('complexity_level', 'medium')
    data.setdefault('has_basement', False)
    data.setdefault('weather_risk_zone', 'moderate')
    data.setdefault('contractor_experience_years', 5)

    try:
        result = predictor.predict(data)
    except Exception as e:
        logger.error(f"Quick estimate failed: {e}")
        return jsonify({'error': 'Estimate failed. Please check your inputs.'}), 500

    return jsonify(result), 200


@bp.route('/compare', methods=['POST'])
@limiter.limit("10 per minute")
def compare_scenarios():
    """Compare multiple project scenarios."""
    data = request.get_json()

    if not data or 'scenarios' not in data:
        return jsonify({'error': 'No scenarios provided'}), 400

    scenarios = data['scenarios']
    if len(scenarios) < 2:
        return jsonify({'error': 'At least 2 scenarios required for comparison'}), 400

    if len(scenarios) > 10:
        return jsonify({'error': 'Maximum 10 scenarios allowed'}), 400

    results = []
    for i, scenario in enumerate(scenarios):
        # Set defaults
        scenario.setdefault('project_type', 'commercial')
        scenario.setdefault('total_area_sqft', 10000)
        scenario.setdefault('num_workers', 20)
        scenario.setdefault('planned_duration_days', 180)

        try:
            prediction = predictor.predict(scenario)
        except Exception as e:
            logger.error(f"Scenario {i} prediction failed: {e}")
            return jsonify({'error': f'Prediction failed for scenario {i + 1}'}), 500

        prediction['scenario_index'] = i
        prediction['scenario_name'] = scenario.get('name', f'Scenario {i + 1}')
        results.append(prediction)

    # Calculate comparison metrics
    costs = [r['predicted_cost'] for r in results]
    delays = [r['predicted_delay_days'] for r in results]
    risks = [r['risk_score'] for r in results]

    comparison = {
        'scenarios': results,
        'summary': {
            'lowest_cost_scenario': results[costs.index(min(costs))]['scenario_name'],
            'lowest_delay_scenario': results[delays.index(min(delays))]['scenario_name'],
            'lowest_risk_scenario': results[risks.index(min(risks))]['scenario_name'],
            'cost_range': {'min': min(costs), 'max': max(costs)},
            'delay_range': {'min': min(delays), 'max': max(delays)},
            'risk_range': {'min': min(risks), 'max': max(risks)}
        }
    }

    return jsonify(comparison), 200


@bp.route('/govt-estimate', methods=['POST'])
@limiter.limit("20 per minute")
def govt_estimate():
    """Generate government tender estimate with detailed BOQ."""
    data = request.get_json()

    if not data:
        return jsonify({'error': 'No data provided'}), 400

    work_type = data.get('work_type', 'building')
    project_type = data.get('project_type', 'commercial')

    # Determine work type from keywords if not specified
    work_name = data.get('work_name', '').lower()
    if not work_type or work_type == 'building':
        if any(kw in work_name for kw in ['road', 'highway', 'path', 'street', 'lane', 'pavement']):
            work_type = 'road'
        elif any(kw in work_name for kw in ['drain', 'nala', 'sewage', 'drainage', 'culvert']):
            work_type = 'drain'
        elif any(kw in work_name for kw in ['bridge', 'flyover', 'overpass']):
            work_type = 'bridge'
        else:
            work_type = 'building'

    try:
        if work_type == 'building':
            estimate = govt_estimator.estimate_building(data)
        elif work_type == 'road':
            estimate = govt_estimator.estimate_road(data)
        elif work_type == 'drain':
            estimate = govt_estimator.estimate_drain(data)
        else:
            estimate = govt_estimator.estimate_building(data)

        # Add metadata — sanitize string inputs
        estimate['work_name'] = sanitize_string(data.get('work_name', '')) or ''
        estimate['work_type'] = work_type
        estimate['project_type'] = project_type
        estimate['tender_number'] = sanitize_string(data.get('tender_number', '')) or ''
        estimate['department'] = sanitize_string(data.get('department', '')) or ''
        estimate['scheme_name'] = sanitize_string(data.get('scheme_name', '')) or ''
        estimate['location'] = sanitize_string(data.get('location', '')) or ''

        # Save to database
        prediction = Prediction(
            project_id=data.get('project_id'),
            input_data=data,
            predicted_cost=estimate['grand_total'],
            predicted_delay_days=0,
            delay_probability=0,
            risk_score=0,
            cost_lower_bound=estimate['grand_total'] * 0.95,
            cost_upper_bound=estimate['grand_total'] * 1.10,
            delay_lower_bound=0,
            delay_upper_bound=0,
            risk_factors=[]
        )
        db.session.add(prediction)
        db.session.commit()

        estimate['prediction_id'] = prediction.id
        return jsonify(estimate), 200

    except Exception as e:
        logger.error(f"Govt estimate failed: {e}")
        return jsonify({'error': 'Estimate generation failed. Please check your inputs.'}), 500


@bp.route('/sor-rates', methods=['GET'])
def get_sor_rates():
    """Get current SOR rates for reference"""
    from app.ml.sor_rates import SOR_RATES, MATERIAL_RATES, LABOR_RATES, OVERHEAD_CHARGES

    return jsonify({
        'sor_rates': SOR_RATES,
        'material_rates': MATERIAL_RATES,
        'labor_rates': LABOR_RATES,
        'overhead_charges': OVERHEAD_CHARGES
    }), 200


@bp.route('/<int:prediction_id>/export/pdf', methods=['GET'])
def export_prediction_pdf(prediction_id):
    """Export a prediction as a PDF report."""
    prediction = Prediction.query.get_or_404(prediction_id)

    company_name = sanitize_string(request.args.get('company_name', '')) or 'Construction Cost Predictor'
    contact_info = sanitize_string(request.args.get('contact_info', '')) or ''

    prediction_data = prediction.to_dict()

    pdf_buffer = pdf_generator.generate_report(
        prediction_data,
        company_name=company_name,
        contact_info=contact_info
    )

    filename = f"cost_estimate_report_{prediction_id}.pdf"

    return send_file(
        pdf_buffer,
        mimetype='application/pdf',
        as_attachment=True,
        download_name=filename
    )


@bp.route('/optimize', methods=['POST'])
@limiter.limit("20 per minute")
def optimize_costs():
    """Analyze project parameters and suggest cost optimizations."""
    data = request.get_json()

    if not data:
        return jsonify({'error': 'No data provided'}), 400

    # If prediction_id is provided, fetch from database
    if 'prediction_id' in data:
        prediction = Prediction.query.get(data['prediction_id'])
        if not prediction:
            return jsonify({'error': 'Prediction not found'}), 404
        input_data = prediction.input_data
        predicted_cost = prediction.predicted_cost
    else:
        input_data = data.get('input_data', {})
        predicted_cost = data.get('predicted_cost', 0)

        if not input_data or predicted_cost <= 0:
            return jsonify({'error': 'Invalid input_data or predicted_cost'}), 400

    try:
        result = cost_optimizer.analyze(input_data, predicted_cost)
    except Exception as e:
        logger.error(f"Cost optimization failed: {e}")
        return jsonify({'error': 'Optimization analysis failed'}), 500

    return jsonify(result), 200


@bp.route('/<int:prediction_id>/optimize', methods=['GET'])
def optimize_prediction(prediction_id):
    """Get optimization suggestions for an existing prediction."""
    prediction = Prediction.query.get_or_404(prediction_id)

    try:
        result = cost_optimizer.analyze(
            prediction.input_data,
            prediction.predicted_cost
        )
    except Exception as e:
        logger.error(f"Cost optimization for prediction {prediction_id} failed: {e}")
        return jsonify({'error': 'Optimization analysis failed'}), 500

    return jsonify(result), 200


@bp.route('/<int:prediction_id>/feedback', methods=['POST'])
@limiter.limit("10 per minute")
def submit_feedback(prediction_id):
    """Submit feedback for a prediction."""
    prediction = Prediction.query.get_or_404(prediction_id)
    data = request.get_json()

    if not data or 'is_useful' not in data:
        return jsonify({'error': 'is_useful field is required'}), 400

    # Sanitize comment
    comment = ''
    if data.get('comment'):
        comment = sanitize_string(data['comment'], max_length=1000) or ''

    feedback = Feedback(
        prediction_id=prediction_id,
        is_useful=bool(data['is_useful']),
        comment=comment
    )

    db.session.add(feedback)
    db.session.commit()
    logger.info(f"Feedback submitted for prediction {prediction_id}: useful={data['is_useful']}")

    return jsonify(feedback.to_dict()), 201


@bp.route('/<int:prediction_id>/feedback', methods=['GET'])
def get_feedback(prediction_id):
    """Get all feedback for a prediction"""
    Prediction.query.get_or_404(prediction_id)
    feedbacks = Feedback.query.filter_by(prediction_id=prediction_id)\
        .order_by(Feedback.created_at.desc()).all()
    return jsonify([f.to_dict() for f in feedbacks]), 200
