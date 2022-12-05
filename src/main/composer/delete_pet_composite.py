from src.data.delete_pet.delete import DeletePet
from src.infra.repo.pet_repository import PetRepository
from src.main.interface import RouteInterface
from src.presenters.controllers.delete_pet_controller import DeletePetController


def delete_pet_composer() -> RouteInterface:
    """
    Composition delete pet route
    :param None
    :return: None
    """
    pet_repository = PetRepository()

    pet_case = DeletePet(pet_repository)
    delete_pet_route = DeletePetController(pet_case)

    return delete_pet_route