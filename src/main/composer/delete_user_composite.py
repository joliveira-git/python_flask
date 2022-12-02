from src.data.delete_user import DeleteUser
from src.infra.repo.pet_repository import PetRepository
from src.infra.repo.user_repository import UserRepository
from src.main.interface import RouteInterface
from src.presenters.controllers import DeleteUserController


def delete_user_composer() -> RouteInterface:
    """
    Composition register user route
    :param None
    :return: None
    """
    user_repository = UserRepository()
    pet_repository = PetRepository()

    user_case = DeleteUser(user_repository, pet_repository)
    delete_user_route = DeleteUserController(user_case)

    return delete_user_route