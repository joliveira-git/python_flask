from typing import Type, Dict

from src.data.interfaces import UserRepositoryInterface as UserRepository
from src.data.interfaces import PetRepositoryInterface as PetRepository
from src.domain.use_cases import DeleteUser as DeleteUserInterface


class DeleteUser(DeleteUserInterface):
    """Class to define usecase: Register User"""
    def __init__(self, user_repository: Type[UserRepository], pet_repository: Type[PetRepository]):
        self.__user_repository = user_repository
        self.__pet_repository = pet_repository

    def delete(self, user_id: int) -> Dict[bool, None]:
        """
        Register user use case
        :param user_id: identification of user
        :return Dictionary with informations of the process
        """
        response = None
        pets = self.__pet_repository.select_pet(user_id=user_id)
        validate_entry = len(pets) == 0

        if validate_entry:
            response = self.__user_repository.delete_user(user_id)

        return {"Success": validate_entry}
