from flask import jsonify, request
from flask_restx import Namespace, Resource, fields

from src.main.adapter import flask_adapter
from src.main.composer import register_user_composer

users_api_ns = Namespace("users", description="pets owner")
user_fields = users_api_ns.model(
    "User", {"name": fields.String, "password": fields.String}
)

class UserList(Resource):
    def get(self):
        """Get a list of articles"""
        # return get_all_articles()

    @users_api_ns.doc(body=user_fields)
    def post(self):
        """register user route"""
        response = flask_adapter(request=request, api_route=register_user_composer())
        if response.status_code < 300:
            message = {
                "type": "users",
                "id": response.body.id,
                "atributes": {"name": response.body.name}
            }
            return jsonify({"data": message}), response.status_code
        return jsonify({
            "error": {
                "status": response.status_code,
                "title": response.body["error"]
            }
        }), response.status_code


class User(Resource):
    def get(self, user_id):
        """Get an user by ID"""
        # return get_article(user_id)

    @users_api_ns.doc(body=user_fields)
    def put(self, user_id):
        """Update an user by ID"""
        # return update_article(user_id, request.get_json())

    def delete(self, user_id):
        """Delete an user by ID"""
        # return delete_article(user_id)


users_api_ns.add_resource(UserList, "")
users_api_ns.add_resource(User, "/<int:user_id>")
