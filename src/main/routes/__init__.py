from flask import Blueprint
from flask_restx import Api

from src.main.routes.health_check_api import health_api_ns
from src.main.routes.user_api import users_api_ns

api_bp = Blueprint("api", __name__)

api = Api(api_bp, title="Flask REST API", description="A REST API build with Flask")

api.add_namespace(health_api_ns)
api.add_namespace(users_api_ns)