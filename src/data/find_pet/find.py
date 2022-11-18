from src.domain.models import Pets
from src.domain.use_cases import FindPet as FindPetInterface
from typing import Type, Dict, List
from src.data.interfaces import PetRepositoryInterface as PetRepository

class FindPet(FindPetInterface):
    """Class to define use case Find Pet"""
    def __init__(self, pet_repository: Type[PetRepository]):
        self.pet_repository = pet_repository

    def by_pet_id(self, pet_id: int) -> Dict[bool, List[Pets]]:
        """
        Select pet by id
        :param - pet_id: id of the pet
        :return - dictionary with informations of the process
        """
        response = None
        validate_entry = isinstance(pet_id, int)
        if validate_entry:
            response = self.pet_repository.select_pet(pet_id=pet_id)

        return {"Success": validate_entry, "Data": response}

    def by_user_id(self, user_id: int) -> Dict[bool, List[Pets]]:
        """
        Select pet by user_id
        :param - user_id: id of the user owner of the pet
        :return - dictionary with informations of the process
        """
        response = None
        validate_entry = isinstance(user_id, str)
        if validate_entry:
            response = self.pet_repository.select_pet(user_id=user_id)

        return {"Success": validate_entry, "Data": response}

    def by_pet_id_and_user_id(self, pet_id: int, user_id: str) -> Dict[bool, List[Pets]]:
        """
        Select pet by pet_id and user_id
        :param - pet_id: id of the pet
               - user_id: id of the user
        :return - dictionary with informations of the process
        """
        response = None
        validate_entry = isinstance(pet_id, int) and isinstance(user_id, int)
        if validate_entry:
            response = self.pet_repository.select_pet(pet_id=pet_id, user_id=user_id)

        return {"Success": validate_entry, "Data": response}