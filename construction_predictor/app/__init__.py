import os
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()

# Get the base directory (parent of app folder)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def create_app(config_class=Config):
    app = Flask(__name__,
                template_folder=os.path.join(BASE_DIR, 'templates'),
                static_folder=os.path.join(BASE_DIR, 'static'))
    app.config.from_object(config_class)

    CORS(app, resources={r"/api/*": {"origins": os.environ.get("ALLOWED_ORIGINS", "*")}})
    db.init_app(app)

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

    return app
