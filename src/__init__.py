from flask import Flask

from src.main.configs.config import config
from src.main.midlewares import db, ma

def create_app(config_name=None):
    app = Flask(__name__)
    app.config.from_object(config.get(config_name or 'default'))

    register_extensions(app)

    from src.main.routes import api_bp
    app.register_blueprint(api_bp, url_prefix="/api")

    return app

def register_extensions(app):
    db.init_app(app)
    ma.init_app(app)
