import os
import secrets
import logging

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    # Issue #2: Generate a strong random SECRET_KEY if not set via env var
    SECRET_KEY = os.environ.get('SECRET_KEY') or secrets.token_hex(32)

    # Issue #13: Support PostgreSQL via DATABASE_URL, fallback to SQLite for local dev
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        f'sqlite:///{os.path.join(BASE_DIR, "construction.db")}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Fix postgres:// scheme for SQLAlchemy (Render uses postgres://, SQLAlchemy needs postgresql://)
    if SQLALCHEMY_DATABASE_URI and SQLALCHEMY_DATABASE_URI.startswith('postgres://'):
        SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace('postgres://', 'postgresql://', 1)

    # Issue #12: Session timeout (30 minutes)
    PERMANENT_SESSION_LIFETIME = 1800  # seconds

    # Issue #3: CORS allowed origins
    ALLOWED_ORIGINS = os.environ.get('ALLOWED_ORIGINS', '').strip()

    # ML Model paths
    COST_MODEL_PATH = os.path.join(BASE_DIR, 'trained_models', 'cost_model.joblib')
    DELAY_MODEL_PATH = os.path.join(BASE_DIR, 'trained_models', 'delay_model.joblib')

    # Feature encoders
    ENCODERS_PATH = os.path.join(BASE_DIR, 'trained_models', 'encoders.joblib')

    # Issue #7: Rate limiting defaults
    RATELIMIT_DEFAULT = "200 per hour"
    RATELIMIT_STORAGE_URI = "memory://"

    # Logging
    LOG_LEVEL = os.environ.get('LOG_LEVEL', 'INFO')
