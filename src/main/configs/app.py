from flask import Flask
from flask_cors import CORS

from src.main.midlewares.extensions import db, ma


def create_app(script_info=None):

    app = Flask(__name__)

    # CORS(app)
    app.config.from_object("src.main.configs.config.DevelopmentConfig")
    register_extensions(app)

    from src.main.routes import api_bp
    app.register_blueprint(api_bp, url_prefix="/api")

    return app

def register_extensions(app):
    db.init_app(app)
    ma.init_app(app)