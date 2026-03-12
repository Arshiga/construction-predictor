import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        f'sqlite:///{os.path.join(BASE_DIR, "construction.db")}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # ML Model paths
    COST_MODEL_PATH = os.path.join(BASE_DIR, 'trained_models', 'cost_model.joblib')
    DELAY_MODEL_PATH = os.path.join(BASE_DIR, 'trained_models', 'delay_model.joblib')

    # Feature encoders
    ENCODERS_PATH = os.path.join(BASE_DIR, 'trained_models', 'encoders.joblib')
