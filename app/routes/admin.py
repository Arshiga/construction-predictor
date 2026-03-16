from flask import Blueprint, request, jsonify, render_template, session, redirect, url_for
from app import db
from app.models.database import Feedback, Prediction
from functools import wraps
import os

bp = Blueprint('admin', __name__, url_prefix='/admin')

# Admin password - set via environment variable or use default
ADMIN_PASSWORD = os.environ.get('ADMIN_PASSWORD', 'admin123')


def admin_required(f):
    """Decorator to require admin login"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('admin_logged_in'):
            if request.is_json:
                return jsonify({'error': 'Unauthorized'}), 401
            return redirect(url_for('admin.login_page'))
        return f(*args, **kwargs)
    return decorated_function


@bp.route('/login', methods=['GET'])
def login_page():
    """Serve admin login page"""
    if session.get('admin_logged_in'):
        return redirect(url_for('admin.dashboard'))
    return render_template('admin_login.html')


@bp.route('/login', methods=['POST'])
def login():
    """Handle admin login"""
    data = request.get_json()
    if not data or 'password' not in data:
        return jsonify({'error': 'Password required'}), 400

    if data['password'] == ADMIN_PASSWORD:
        session['admin_logged_in'] = True
        return jsonify({'success': True}), 200
    else:
        return jsonify({'error': 'Invalid password'}), 401


@bp.route('/logout', methods=['POST'])
def logout():
    """Handle admin logout"""
    session.pop('admin_logged_in', None)
    return jsonify({'success': True}), 200


@bp.route('/dashboard')
@admin_required
def dashboard():
    """Serve admin feedback dashboard"""
    return render_template('admin_dashboard.html')


@bp.route('/api/feedbacks', methods=['GET'])
@admin_required
def get_all_feedbacks():
    """Get all feedbacks with prediction details"""
    feedbacks = Feedback.query.order_by(Feedback.created_at.desc()).all()

    result = []
    for f in feedbacks:
        feedback_data = f.to_dict()
        # Include prediction details
        prediction = Prediction.query.get(f.prediction_id)
        if prediction:
            feedback_data['prediction'] = {
                'id': prediction.id,
                'predicted_cost': prediction.predicted_cost,
                'predicted_delay_days': prediction.predicted_delay_days,
                'risk_score': prediction.risk_score,
                'input_data': prediction.input_data,
                'created_at': prediction.created_at.isoformat() if prediction.created_at else None,
            }
        result.append(feedback_data)

    return jsonify(result), 200


@bp.route('/api/feedbacks/stats', methods=['GET'])
@admin_required
def get_feedback_stats():
    """Get feedback statistics"""
    total = Feedback.query.count()
    useful = Feedback.query.filter_by(is_useful=True).count()
    not_useful = Feedback.query.filter_by(is_useful=False).count()
    with_comments = Feedback.query.filter(Feedback.comment.isnot(None), Feedback.comment != '').count()

    return jsonify({
        'total': total,
        'useful': useful,
        'not_useful': not_useful,
        'with_comments': with_comments,
        'useful_percentage': round((useful / total * 100), 1) if total > 0 else 0,
    }), 200


@bp.route('/api/feedbacks/<int:feedback_id>', methods=['DELETE'])
@admin_required
def delete_feedback(feedback_id):
    """Delete a feedback entry"""
    feedback = Feedback.query.get_or_404(feedback_id)
    db.session.delete(feedback)
    db.session.commit()
    return jsonify({'success': True}), 200
