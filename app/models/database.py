from datetime import datetime
from app import db


class Project(db.Model):
    """Model for construction projects"""
    __tablename__ = 'projects'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    project_type = db.Column(db.String(50), nullable=False)  # residential, commercial, industrial, infrastructure
    location = db.Column(db.String(100), nullable=False)
    total_area_sqft = db.Column(db.Float, nullable=False)
    num_floors = db.Column(db.Integer, default=1)
    num_workers = db.Column(db.Integer, nullable=False)
    planned_duration_days = db.Column(db.Integer, nullable=False)
    material_quality = db.Column(db.String(20), default='standard')  # economy, standard, premium
    complexity_level = db.Column(db.String(20), default='medium')  # low, medium, high
    has_basement = db.Column(db.Boolean, default=False)
    weather_risk_zone = db.Column(db.String(20), default='moderate')  # low, moderate, high
    contractor_experience_years = db.Column(db.Integer, default=5)

    # Actual values (filled after project completion)
    actual_cost = db.Column(db.Float, nullable=True)
    actual_duration_days = db.Column(db.Integer, nullable=True)

    # Timestamps
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    predictions = db.relationship('Prediction', backref='project', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'project_type': self.project_type,
            'location': self.location,
            'total_area_sqft': self.total_area_sqft,
            'num_floors': self.num_floors,
            'num_workers': self.num_workers,
            'planned_duration_days': self.planned_duration_days,
            'material_quality': self.material_quality,
            'complexity_level': self.complexity_level,
            'has_basement': self.has_basement,
            'weather_risk_zone': self.weather_risk_zone,
            'contractor_experience_years': self.contractor_experience_years,
            'actual_cost': self.actual_cost,
            'actual_duration_days': self.actual_duration_days,
            'created_at': self.created_at.isoformat() if self.created_at else None,
        }


class Prediction(db.Model):
    """Model for storing predictions made"""
    __tablename__ = 'predictions'

    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=True)

    # Prediction inputs (snapshot at prediction time)
    input_data = db.Column(db.JSON, nullable=False)

    # Predictions
    predicted_cost = db.Column(db.Float, nullable=False)
    predicted_delay_days = db.Column(db.Float, nullable=False)
    delay_probability = db.Column(db.Float, nullable=False)  # 0-1 probability of any delay
    risk_score = db.Column(db.Float, nullable=False)  # Combined risk score 0-100

    # Confidence intervals
    cost_lower_bound = db.Column(db.Float)
    cost_upper_bound = db.Column(db.Float)
    delay_lower_bound = db.Column(db.Float)
    delay_upper_bound = db.Column(db.Float)

    # Risk factors identified
    risk_factors = db.Column(db.JSON)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'project_id': self.project_id,
            'input_data': self.input_data,
            'predicted_cost': self.predicted_cost,
            'predicted_delay_days': self.predicted_delay_days,
            'delay_probability': self.delay_probability,
            'risk_score': self.risk_score,
            'cost_lower_bound': self.cost_lower_bound,
            'cost_upper_bound': self.cost_upper_bound,
            'delay_lower_bound': self.delay_lower_bound,
            'delay_upper_bound': self.delay_upper_bound,
            'risk_factors': self.risk_factors,
            'created_at': self.created_at.isoformat() if self.created_at else None,
        }
