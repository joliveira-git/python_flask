from typing import Type
from src.domain.use_cases import RegisterPet
from src.presenters.helpers import HttpRequest, HttpResponse
from src.presenters.errors import HttpErrors

class RegisterPetController:
    """Class to define route to register_pet use case"""

    def __init__(self, register_pet_use_case: Type[RegisterPet]):
        self.register_pet_use_case = register_pet_use_case

    def route(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """Method to call use case"""

        if http_request.body:
            name = http_request.body.get("name")
            specie = http_request.body.get("specie")
            user_information = http_request.body.get("user_information")
            age = http_request.body.get("age")

            if name and specie and user_information and ("user_id" in user_information or "user_name" in user_information):
                response = self.register_pet_use_case.registry(name, specie, user_information, age)
            else:
                http_error = HttpErrors.error_422()
                return HttpResponse(status_code=http_error["status_code"], body=http_error["body"])
        else:
            http_error = HttpErrors.error_400()
            return HttpResponse(status_code=http_error["status_code"], body=http_error["body"])

        return HttpResponse(status_code=200, body=response["Data"])
