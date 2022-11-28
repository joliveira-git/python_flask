from flask import jsonify, request
from flask_restx import Namespace, Resource, fields

from src.main.adapter import flask_adapter
from src.main.composer import register_user_composer, find_user_composer
from src.main.serializer.users_serializer import UsersSerializer

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
            data = UsersSerializer.serializer([response.body])
            response = {"data": data}, response.status_code
        else:
            response = {
                "error": {
                    "status": response.status_code,
                    "title": response.body["error"]
                }
            }, response.status_code

        return response

class User(Resource):
    def get(self, user_id):
        """Get an user by ID"""
        response = flask_adapter(request=request, api_route=find_user_composer())
        if response.status_code < 300:
            data = UsersSerializer.serializer(response.body)
            response = {"data": data}, response.status_code
        else:
            response = {
                "error": {
                    "status": response.status_code,
                    "title": response.body["error"]
                }
            }, response.status_code

        return response

    @users_api_ns.doc(body=user_fields)
    def put(self, user_id):
        """Update an user by ID"""
        # return update_article(user_id, request.get_json())

    def delete(self, user_id):
        """Delete an user by ID"""
        # return delete_article(user_id)


users_api_ns.add_resource(UserList, "")
users_api_ns.add_resource(User, "/<int:user_id>")
