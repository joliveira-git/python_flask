from typing import Type
from src.main.interface import RouteInterface
from src.domain.use_cases import DeleteUser
from src.presenters.helpers import HttpRequest, HttpResponse
from src.presenters.errors import HttpErrors


class DeletePetController(RouteInterface):
    """ Class to Define Route to delete_pet use case """

    def __init__(self, delete_pet_use_case: Type[DeleteUser]):
        self.delete_pet_use_case = delete_pet_use_case

    def route(self, http_request: Type[HttpRequest]) -> HttpResponse:
        """ Method to call use case """

        if http_request.query:
            query_string_params = http_request.query.keys()

            if "pet_id" in query_string_params:
                pet_id = http_request.query["pet_id"]
                response = self.delete_pet_use_case.delete(pet_id)
            else:
                response = {"Success": False, "Data": None}

            if response["Success"] is False:
                https_error = HttpErrors.error_422()
                return HttpResponse(
                    status_code=https_error["status_code"], body=https_error["body"], detail="could not delete record"
                )

            return HttpResponse(status_code=200, body={}, detail="successfully deleted record")

        https_error = HttpErrors.error_400()
        return HttpResponse(
            status_code=https_error["status_code"], body=https_error["body"], detail="invalid request message"
        )