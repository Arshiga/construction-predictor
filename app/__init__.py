import os
import logging
from datetime import timedelta
from flask import Flask, session
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from config import Config

db = SQLAlchemy()
migrate = Migrate()
limiter = Limiter(key_func=get_remote_address, default_limits=["200 per hour"])

# Get the base directory (parent of app folder)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def create_app(config_class=Config):
    app = Flask(__name__,
                template_folder=os.path.join(BASE_DIR, 'templates'),
                static_folder=os.path.join(BASE_DIR, 'static'))
    app.config.from_object(config_class)

    # Issue #9: Configure proper logging
    log_level = getattr(logging, app.config.get('LOG_LEVEL', 'INFO'), logging.INFO)
    logging.basicConfig(
        level=log_level,
        format='%(asctime)s [%(levelname)s] %(name)s: %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    app.logger.setLevel(log_level)

    # Issue #3: CORS — restrict origins in production
    allowed_origins = app.config.get('ALLOWED_ORIGINS', '')
    if allowed_origins:
        origins = [o.strip() for o in allowed_origins.split(',') if o.strip()]
    else:
        origins = "*"  # Allow all in development only
    CORS(app, resources={r"/api/*": {"origins": origins}})

    # Issue #12: Session timeout — make sessions permanent with expiry
    app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(
        seconds=app.config.get('PERMANENT_SESSION_LIFETIME', 1800)
    )

    @app.before_request
    def make_session_permanent():
        session.permanent = True

    # Issue #18: Security headers
    @app.after_request
    def set_security_headers(response):
        response.headers['X-Content-Type-Options'] = 'nosniff'
        response.headers['X-Frame-Options'] = 'SAMEORIGIN'
        response.headers['X-XSS-Protection'] = '1; mode=block'
        response.headers['Referrer-Policy'] = 'strict-origin-when-cross-origin'
        return response

    db.init_app(app)
    migrate.init_app(app, db)
    limiter.init_app(app)

    from app.routes import predictions, projects, rates
    from app.routes import admin
    app.register_blueprint(predictions.bp)
    app.register_blueprint(projects.bp)
    app.register_blueprint(rates.bp)
    app.register_blueprint(admin.bp)

    from app.routes.main import main_bp
    app.register_blueprint(main_bp)

    with app.app_context():
        db.create_all()

    app.logger.info("Application started successfully")
    return app
