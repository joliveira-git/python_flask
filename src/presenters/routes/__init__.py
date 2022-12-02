from flask import Blueprint
from flask_restx import Api

from src.presenters.routes.health_check_api import health_api_ns
from src.presenters.routes.user_api import users_api_ns
from src.presenters.routes.pets_api import pets_api_ns

api_bp = Blueprint("api", __name__)

api = Api(api_bp, title="MyPet - Flask REST API", description="A REST API built in Python and Flask using Clean Architecture")

api.add_namespace(health_api_ns)
api.add_namespace(users_api_ns)
api.add_namespace(pets_api_ns)