from src.data.find_user import FindUser
from src.main.interface import RouteInterface
from src.presenters.controllers import RegisterUserController, FindUserController
from src.data.register_user import RegisterUser
from src.infra.repo.user_repository import UserRepository


def register_user_composer() -> RouteInterface:
    """
    Composition register user route
    :param None
    :return: Object with register user route
    """
    repository = UserRepository()
    user_case = RegisterUser(repository)
    register_user_route = RegisterUserController(user_case)

    return register_user_route

def find_user_composer() -> RouteInterface:
    """
    Composition register user route
    :param None
    :return: Object with register user route
    """
    repository = UserRepository()
    user_case = FindUser(repository)
    find_user_route = FindUserController(user_case)

    return find_user_route