from typing import Type, Dict

from src.data.interfaces import PetRepositoryInterface as PetRepository
from src.domain.use_cases import DeletePet as DeletePetInterface


class DeletePet(DeletePetInterface):
    """Class to define usecase: Register Pet"""
    def __init__(self, pet_repository: Type[PetRepository]):
        self.__pet_repository = pet_repository

    def delete(self, pet_id: int) -> Dict[str, bool]:
        """
        Register pet use case
        :param pet_id: identification of pet
        :return Dictionary with informations of the process
        """
        self.__pet_repository.delete_pet(pet_id)

        return {"Success": True}
