"""
Application Factory
"""

from flask import Flask
from .config import Config
from .main import main_bp
from .admin import admin_bp

def create_app():
    """Initialize Flask application"""
    app = Flask(__name__)
    app.logger.info('Application started')
    app.config.from_object(Config)


    app.register_blueprint(main_bp)
    app.register_blueprint(admin_bp)

    return app
