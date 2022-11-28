from src.data.find_pet import FindPet
from src.main.interface import RouteInterface
from src.presenters.controllers import RegisterPetController, FindPetController
from src.data.register_pet import RegisterPet
from src.infra.repo.pet_repository import PetRepository


def register_pet_composer() -> RouteInterface:
    """
    Composition register pet route
    :param None
    :return: Object with register pet route
    """
    repository = PetRepository()
    pet_case = RegisterPet(repository)
    register_pet_route = RegisterPetController(pet_case)

    return register_pet_route

def find_pet_composer() -> RouteInterface:
    """
    Composition register pet route
    :param None
    :return: Object with register pet route
    """
    repository = PetRepository()
    pet_case = FindPet(repository)
    find_pet_route = FindPetController(pet_case)

    return find_pet_route