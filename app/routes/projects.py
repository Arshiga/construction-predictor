import logging
from flask import Blueprint, request, jsonify, session
from app import db, limiter
from app.models.database import Project, Prediction
from functools import wraps

bp = Blueprint('projects', __name__, url_prefix='/api/projects')
logger = logging.getLogger(__name__)

# --- Issue #8: Authentication for destructive operations ---

VALID_PROJECT_TYPES = {'residential', 'commercial', 'industrial', 'infrastructure'}
VALID_MATERIAL_QUALITY = {'economy', 'standard', 'premium'}
VALID_COMPLEXITY = {'low', 'medium', 'high'}
VALID_WEATHER_RISK = {'low', 'moderate', 'high'}


def auth_required(f):
    """Require admin login for sensitive operations"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('admin_logged_in'):
            return jsonify({'error': 'Authentication required. Please login as admin.'}), 401
        return f(*args, **kwargs)
    return decorated_function


@bp.route('', methods=['GET'])
def get_projects():
    """Get all projects"""
    projects = Project.query.order_by(Project.created_at.desc()).all()
    return jsonify([p.to_dict() for p in projects]), 200


@bp.route('', methods=['POST'])
@limiter.limit("20 per minute")
def create_project():
    """Create a new project"""
    data = request.get_json()

    if not data:
        return jsonify({'error': 'No data provided'}), 400

    required_fields = ['name', 'project_type', 'total_area_sqft', 'num_workers', 'planned_duration_days']
    missing_fields = [f for f in required_fields if f not in data]
    if missing_fields:
        return jsonify({'error': f'Missing required fields: {missing_fields}'}), 400

    # Issue #5 & #6: Validate inputs
    errors = []

    if data.get('project_type') not in VALID_PROJECT_TYPES:
        errors.append(f"Invalid project_type. Must be one of: {', '.join(VALID_PROJECT_TYPES)}")

    try:
        area = float(data['total_area_sqft'])
        if area <= 0 or area > 10000000:
            errors.append("total_area_sqft must be between 1 and 10,000,000")
    except (ValueError, TypeError):
        errors.append("total_area_sqft must be a number")

    try:
        workers = int(data['num_workers'])
        if workers <= 0 or workers > 50000:
            errors.append("num_workers must be between 1 and 50,000")
    except (ValueError, TypeError):
        errors.append("num_workers must be a number")

    try:
        days = int(data['planned_duration_days'])
        if days <= 0 or days > 36500:
            errors.append("planned_duration_days must be between 1 and 36,500")
    except (ValueError, TypeError):
        errors.append("planned_duration_days must be a number")

    if 'material_quality' in data and data['material_quality'] not in VALID_MATERIAL_QUALITY:
        errors.append(f"Invalid material_quality. Must be one of: {', '.join(VALID_MATERIAL_QUALITY)}")

    if 'complexity_level' in data and data['complexity_level'] not in VALID_COMPLEXITY:
        errors.append(f"Invalid complexity_level. Must be one of: {', '.join(VALID_COMPLEXITY)}")

    if 'weather_risk_zone' in data and data['weather_risk_zone'] not in VALID_WEATHER_RISK:
        errors.append(f"Invalid weather_risk_zone. Must be one of: {', '.join(VALID_WEATHER_RISK)}")

    if errors:
        return jsonify({'error': 'Validation failed', 'details': errors}), 400

    project = Project(
        name=data['name'][:200],  # Limit name length
        project_type=data['project_type'],
        location=data.get('location', 'Unknown')[:200],
        total_area_sqft=data['total_area_sqft'],
        num_floors=data.get('num_floors', 1),
        num_workers=data['num_workers'],
        planned_duration_days=data['planned_duration_days'],
        material_quality=data.get('material_quality', 'standard'),
        complexity_level=data.get('complexity_level', 'medium'),
        has_basement=data.get('has_basement', False),
        weather_risk_zone=data.get('weather_risk_zone', 'moderate'),
        contractor_experience_years=data.get('contractor_experience_years', 5)
    )

    db.session.add(project)
    db.session.commit()
    logger.info(f"Project {project.id} created: {project.name}")

    return jsonify(project.to_dict()), 201


@bp.route('/<int:project_id>', methods=['GET'])
def get_project(project_id):
    """Get a specific project"""
    project = Project.query.get_or_404(project_id)
    result = project.to_dict()

    # Include predictions for this project
    predictions = Prediction.query.filter_by(project_id=project_id).order_by(
        Prediction.created_at.desc()
    ).all()
    result['predictions'] = [p.to_dict() for p in predictions]

    return jsonify(result), 200


@bp.route('/<int:project_id>', methods=['PUT'])
@auth_required  # Issue #8: Require auth for modifications
def update_project(project_id):
    """Update a project"""
    project = Project.query.get_or_404(project_id)
    data = request.get_json()

    if not data:
        return jsonify({'error': 'No data provided'}), 400

    # Update fields
    updatable_fields = [
        'name', 'project_type', 'location', 'total_area_sqft', 'num_floors',
        'num_workers', 'planned_duration_days', 'material_quality',
        'complexity_level', 'has_basement', 'weather_risk_zone',
        'contractor_experience_years', 'actual_cost', 'actual_duration_days'
    ]

    for field in updatable_fields:
        if field in data:
            setattr(project, field, data[field])

    db.session.commit()
    logger.info(f"Project {project_id} updated by admin")
    return jsonify(project.to_dict()), 200


@bp.route('/<int:project_id>', methods=['DELETE'])
@auth_required  # Issue #8: Require auth for deletion
def delete_project(project_id):
    """Delete a project — admin only"""
    project = Project.query.get_or_404(project_id)

    # Delete associated predictions
    Prediction.query.filter_by(project_id=project_id).delete()

    db.session.delete(project)
    db.session.commit()
    logger.warning(f"Project {project_id} deleted by admin from {request.remote_addr}")

    return jsonify({'message': 'Project deleted successfully'}), 200


@bp.route('/<int:project_id>/complete', methods=['POST'])
@auth_required  # Issue #8: Require auth for completing projects
def complete_project(project_id):
    """Mark a project as complete with actual values."""
    project = Project.query.get_or_404(project_id)
    data = request.get_json()

    if not data:
        return jsonify({'error': 'No data provided'}), 400

    if 'actual_cost' not in data or 'actual_duration_days' not in data:
        return jsonify({'error': 'Both actual_cost and actual_duration_days are required'}), 400

    # Validate actual values
    try:
        actual_cost = float(data['actual_cost'])
        if actual_cost <= 0:
            return jsonify({'error': 'actual_cost must be positive'}), 400
    except (ValueError, TypeError):
        return jsonify({'error': 'actual_cost must be a number'}), 400

    try:
        actual_days = int(data['actual_duration_days'])
        if actual_days <= 0:
            return jsonify({'error': 'actual_duration_days must be positive'}), 400
    except (ValueError, TypeError):
        return jsonify({'error': 'actual_duration_days must be a number'}), 400

    project.actual_cost = actual_cost
    project.actual_duration_days = actual_days

    db.session.commit()
    logger.info(f"Project {project_id} marked complete: cost={actual_cost}, days={actual_days}")

    # Calculate accuracy of predictions
    predictions = Prediction.query.filter_by(project_id=project_id).all()
    accuracy_report = []

    for pred in predictions:
        cost_error = abs(pred.predicted_cost - project.actual_cost) / project.actual_cost * 100
        delay_actual = project.actual_duration_days - project.planned_duration_days
        delay_error = abs(pred.predicted_delay_days - delay_actual)

        accuracy_report.append({
            'prediction_id': pred.id,
            'cost_error_percent': round(cost_error, 2),
            'delay_error_days': round(delay_error, 1),
            'predicted_cost': pred.predicted_cost,
            'actual_cost': project.actual_cost,
            'predicted_delay': pred.predicted_delay_days,
            'actual_delay': delay_actual
        })

    return jsonify({
        'project': project.to_dict(),
        'accuracy_report': accuracy_report
    }), 200


@bp.route('/stats', methods=['GET'])
def get_stats():
    """Get overall statistics"""
    total_projects = Project.query.count()
    completed_projects = Project.query.filter(Project.actual_cost.isnot(None)).count()
    total_predictions = Prediction.query.count()

    # Calculate average risk score
    from sqlalchemy import func
    avg_risk = db.session.query(func.avg(Prediction.risk_score)).scalar() or 0

    # Project type distribution
    type_counts = db.session.query(
        Project.project_type,
        func.count(Project.id)
    ).group_by(Project.project_type).all()

    return jsonify({
        'total_projects': total_projects,
        'completed_projects': completed_projects,
        'total_predictions': total_predictions,
        'average_risk_score': round(avg_risk, 1),
        'project_type_distribution': {t: c for t, c in type_counts}
    }), 200
