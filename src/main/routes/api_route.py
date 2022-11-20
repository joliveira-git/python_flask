from flask import Blueprint, jsonify
from src.main.composer import register_user_composer
from src.presenters.helpers import HttpResponse

api_routes_bp = Blueprint("api_routes", __name__)

@api_routes_bp.route("/api", methods=["GET"])
def health_check():
    """health check"""
    response = {"status_code": 200, "body": "I'm alive"}
    return jsonify(response)