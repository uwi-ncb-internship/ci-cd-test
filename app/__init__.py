"""
Application Factory
"""

from flask import Flask
from .config import Config

def create_app():
    app = Flask(__name__)
    app.logger.info('Application started')
    app.config.from_object(Config)

    from .main import main_bp
    from .admin import admin_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(admin_bp)

    return app
