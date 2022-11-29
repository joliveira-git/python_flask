from flask import jsonify, request
from flask_restx import Namespace, Resource, fields

from src.main.adapter import flask_adapter
from src.main.composer import register_pet_composer, find_pet_composer
from src.main.serializer.pets_serializer import PetsSerializer

pets_api_ns = Namespace("pets", description="pets")
pet_fields = pets_api_ns.model(
    "Pet", {"id": fields.Integer, "name": fields.String, "specie": fields.String, "age": fields.Integer, "user_information": fields.Nested}
)

class PetList(Resource):
    def get(self):
        """Get a list of pets"""
        # return get_all_articles()

    @pets_api_ns.doc(body=pet_fields)
    def post(self):
        """register pet route"""
        response = flask_adapter(request=request, api_route=register_pet_composer())
        if response.status_code < 300:
            data = PetsSerializer.serializer([response.body])
            response = {"data": data}, response.status_code
        else:
            response = {
                "error": {
                    "status": response.status_code,
                    "title": response.body["error"]
                }
            }, response.status_code

        return response

class Pet(Resource):
    def get(self, pet_id):
        """Get an pet by ID"""
        response = flask_adapter(request=request, api_route=find_pet_composer())
        if response.status_code < 300:
            data = PetsSerializer.serializer(response.body)
            response = {"data": data}, response.status_code
        else:
            response = {
                "error": {
                    "status": response.status_code,
                    "title": response.body["error"]
                }
            }, response.status_code

        return response

    @pets_api_ns.doc(body=pet_fields)
    def put(self, pet_id):
        """Update an pet by ID"""
        # return update_article(pet_id, request.get_json())

    def delete(self, pet_id):
        """Delete an pet by ID"""
        # return delete_article(pet_id)


pets_api_ns.add_resource(PetList, "")
pets_api_ns.add_resource(Pet, "/<int:pet_id>")
