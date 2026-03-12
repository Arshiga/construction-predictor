from flask import Blueprint, request, jsonify
from app import db
from app.models.database import Project, Prediction

bp = Blueprint('projects', __name__, url_prefix='/api/projects')


@bp.route('', methods=['GET'])
def get_projects():
    """Get all projects"""
    projects = Project.query.order_by(Project.created_at.desc()).all()
    return jsonify([p.to_dict() for p in projects]), 200


@bp.route('', methods=['POST'])
def create_project():
    """Create a new project"""
    data = request.get_json()

    if not data:
        return jsonify({'error': 'No data provided'}), 400

    required_fields = ['name', 'project_type', 'total_area_sqft', 'num_workers', 'planned_duration_days']
    missing_fields = [f for f in required_fields if f not in data]
    if missing_fields:
        return jsonify({'error': f'Missing required fields: {missing_fields}'}), 400

    project = Project(
        name=data['name'],
        project_type=data['project_type'],
        location=data.get('location', 'Unknown'),
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
    return jsonify(project.to_dict()), 200


@bp.route('/<int:project_id>', methods=['DELETE'])
def delete_project(project_id):
    """Delete a project"""
    project = Project.query.get_or_404(project_id)

    # Delete associated predictions
    Prediction.query.filter_by(project_id=project_id).delete()

    db.session.delete(project)
    db.session.commit()

    return jsonify({'message': 'Project deleted successfully'}), 200


@bp.route('/<int:project_id>/complete', methods=['POST'])
def complete_project(project_id):
    """
    Mark a project as complete with actual values.
    This data can be used for model training.
    """
    project = Project.query.get_or_404(project_id)
    data = request.get_json()

    if not data:
        return jsonify({'error': 'No data provided'}), 400

    if 'actual_cost' not in data or 'actual_duration_days' not in data:
        return jsonify({'error': 'Both actual_cost and actual_duration_days are required'}), 400

    project.actual_cost = data['actual_cost']
    project.actual_duration_days = data['actual_duration_days']

    db.session.commit()

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
