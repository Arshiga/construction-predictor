from flask import Blueprint, request, jsonify, send_file
from app import db
from app.models.database import Project, Prediction, Feedback
from app.ml.predictor import CostDelayPredictor
from app.ml.govt_estimator import GovtCostEstimator
from app.services.pdf_generator import pdf_generator
from app.services.cost_optimizer import cost_optimizer
import os

bp = Blueprint('predictions', __name__, url_prefix='/api/predictions')

# Initialize predictor
MODEL_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'trained_models')
predictor = CostDelayPredictor(model_dir=MODEL_DIR)

# Initialize government estimator
govt_estimator = GovtCostEstimator()


@bp.route('/predict', methods=['POST'])
def make_prediction():
    """
    Make a cost and delay prediction for a construction project.

    Expected JSON body:
    {
        "project_type": "residential|commercial|industrial|infrastructure",
        "location": "string",
        "total_area_sqft": float,
        "num_floors": int,
        "num_workers": int,
        "planned_duration_days": int,
        "material_quality": "economy|standard|premium",
        "complexity_level": "low|medium|high",
        "has_basement": bool,
        "weather_risk_zone": "low|moderate|high",
        "contractor_experience_years": int,
        "project_id": int (optional - to link prediction to existing project)
    }
    """
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
    # New detailed fields
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

    # Make prediction
    result = predictor.predict(data)

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
def quick_estimate():
    """
    Get a quick estimate without saving to database.
    Useful for real-time form feedback.
    """
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

    result = predictor.predict(data)
    return jsonify(result), 200


@bp.route('/compare', methods=['POST'])
def compare_scenarios():
    """
    Compare multiple project scenarios.

    Expected JSON body:
    {
        "scenarios": [
            { ...project_data... },
            { ...project_data... }
        ]
    }
    """
    data = request.get_json()

    if not data or 'scenarios' not in data:
        return jsonify({'error': 'No scenarios provided'}), 400

    scenarios = data['scenarios']
    if len(scenarios) < 2:
        return jsonify({'error': 'At least 2 scenarios required for comparison'}), 400

    results = []
    for i, scenario in enumerate(scenarios):
        # Set defaults
        scenario.setdefault('project_type', 'commercial')
        scenario.setdefault('total_area_sqft', 10000)
        scenario.setdefault('num_workers', 20)
        scenario.setdefault('planned_duration_days', 180)

        prediction = predictor.predict(scenario)
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
def govt_estimate():
    """
    Generate government tender estimate with detailed BOQ.
    Based on SOR/DSR rates.

    Expected JSON body:
    {
        "work_name": "Construction of Community Hall",
        "project_type": "commercial",  # residential, commercial, industrial, infrastructure
        "work_type": "building",  # building, road, drain, culvert
        "total_area_sqft": 5000,
        "num_floors": 2,
        "location": "Mumbai, Maharashtra",
        "material_quality": "standard",
        "complexity_level": "medium",
        "has_basement": false,

        # For road work
        "road_length_m": 1000,
        "road_width_m": 7,
        "road_type": "bituminous",

        # For drain work
        "drain_length_m": 500,
        "drain_width_m": 1.0,
        "drain_depth_m": 0.6,
        "drain_type": "open"
    }
    """
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

        # Add metadata
        estimate['work_name'] = data.get('work_name', '')
        estimate['work_type'] = work_type
        estimate['project_type'] = project_type
        estimate['tender_number'] = data.get('tender_number', '')
        estimate['department'] = data.get('department', '')
        estimate['scheme_name'] = data.get('scheme_name', '')
        estimate['location'] = data.get('location', '')

        # Save to database
        prediction = Prediction(
            project_id=data.get('project_id'),
            input_data=data,
            predicted_cost=estimate['grand_total'],
            predicted_delay_days=0,  # BOQ doesn't predict delay
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
        return jsonify({'error': str(e)}), 500


@bp.route('/sor-rates', methods=['GET'])
def get_sor_rates():
    """
    Get current SOR rates for reference
    """
    from app.ml.sor_rates import SOR_RATES, MATERIAL_RATES, LABOR_RATES, OVERHEAD_CHARGES

    return jsonify({
        'sor_rates': SOR_RATES,
        'material_rates': MATERIAL_RATES,
        'labor_rates': LABOR_RATES,
        'overhead_charges': OVERHEAD_CHARGES
    }), 200


@bp.route('/<int:prediction_id>/export/pdf', methods=['GET'])
def export_prediction_pdf(prediction_id):
    """
    Export a prediction as a PDF report.

    Query parameters:
        company_name: Optional company name for report branding
        contact_info: Optional contact information for report header
    """
    prediction = Prediction.query.get_or_404(prediction_id)

    # Get optional branding parameters
    company_name = request.args.get('company_name', 'Construction Cost Predictor')
    contact_info = request.args.get('contact_info', '')

    # Convert prediction to dictionary
    prediction_data = prediction.to_dict()

    # Generate PDF
    pdf_buffer = pdf_generator.generate_report(
        prediction_data,
        company_name=company_name,
        contact_info=contact_info
    )

    # Generate filename
    filename = f"cost_estimate_report_{prediction_id}.pdf"

    return send_file(
        pdf_buffer,
        mimetype='application/pdf',
        as_attachment=True,
        download_name=filename
    )


@bp.route('/optimize', methods=['POST'])
def optimize_costs():
    """
    Analyze project parameters and suggest cost optimizations.

    Expected JSON body:
    {
        "input_data": { ...project parameters... },
        "predicted_cost": float
    }

    Or with prediction_id:
    {
        "prediction_id": int
    }
    """
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
        # Use provided data
        input_data = data.get('input_data', {})
        predicted_cost = data.get('predicted_cost', 0)

        if not input_data or predicted_cost <= 0:
            return jsonify({'error': 'Invalid input_data or predicted_cost'}), 400

    # Run optimization analysis
    result = cost_optimizer.analyze(input_data, predicted_cost)

    return jsonify(result), 200


@bp.route('/<int:prediction_id>/optimize', methods=['GET'])
def optimize_prediction(prediction_id):
    """
    Get optimization suggestions for an existing prediction.
    """
    prediction = Prediction.query.get_or_404(prediction_id)

    result = cost_optimizer.analyze(
        prediction.input_data,
        prediction.predicted_cost
    )

    return jsonify(result), 200


@bp.route('/<int:prediction_id>/feedback', methods=['POST'])
def submit_feedback(prediction_id):
    """
    Submit feedback for a prediction.

    Expected JSON body:
    {
        "is_useful": true/false,
        "comment": "optional comment text"
    }
    """
    prediction = Prediction.query.get_or_404(prediction_id)
    data = request.get_json()

    if not data or 'is_useful' not in data:
        return jsonify({'error': 'is_useful field is required'}), 400

    feedback = Feedback(
        prediction_id=prediction_id,
        is_useful=data['is_useful'],
        comment=data.get('comment', '').strip()[:1000]
    )

    db.session.add(feedback)
    db.session.commit()

    return jsonify(feedback.to_dict()), 201


@bp.route('/<int:prediction_id>/feedback', methods=['GET'])
def get_feedback(prediction_id):
    """Get all feedback for a prediction"""
    Prediction.query.get_or_404(prediction_id)
    feedbacks = Feedback.query.filter_by(prediction_id=prediction_id)\
        .order_by(Feedback.created_at.desc()).all()
    return jsonify([f.to_dict() for f in feedbacks]), 200
