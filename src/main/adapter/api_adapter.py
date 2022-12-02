from typing import Type
from sqlalchemy.exc import IntegrityError
from src.main.interface import RouteInterface as Route
from src.presenters.helpers import HttpRequest, HttpResponse
from src.presenters.errors import HttpErrors

def flask_adapter(request: any, api_route: Type[Route]) -> any:
    """
    Adapter pattern to Flask
    :param request: Flask request
    :param api_route: Composite routes
    :return: Anything
    """
    http_request = HttpRequest(body=request.json if request.is_json else None, query=request.view_args)

    try:
        response = api_route.route(http_request)
    except IntegrityError as e:
        http_error = HttpErrors.error_409()
        return HttpResponse(
            status_code=http_error["status_code"], body=http_error["body"], detail=str(e)
        )
    except Exception as e:
        http_error = HttpErrors.error_400()
        return HttpResponse(
            status_code=http_error["status_code"], body=http_error["body"], detail=str(e)
        )

    return response