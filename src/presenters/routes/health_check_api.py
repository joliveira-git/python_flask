from flask_restx import Namespace, Resource

health_api_ns = Namespace("health", description="Health check related operations")


class Health(Resource):
    def get(self):
        return {"status": "OK", "message": "Server is healthy"}


health_api_ns.add_resource(Health, "")
