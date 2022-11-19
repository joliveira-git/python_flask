from typing import Type, Dict

from src.domain.models import Users
from src.domain.use_cases import RegisterUser as RegisterUserInterface
from src.data.interfaces import UserRepositoryInterface as UserRepository

class RegisterUser(RegisterUserInterface):
    """Class to define usecase: Register User"""
    def __init__(self, user_repository: Type[UserRepository]):
        self.__user_repository = user_repository

    def register(self, name: str, password: str) -> Dict[bool, Users]:
        """
        Register user use case
        :param name: person name
        :param password: password of the person
        :return Dictionary with informations of the process
        """
        response = None
        validate_entry = isinstance(name, str) and isinstance(password, str)

        if validate_entry:
            response = self.__user_repository.insert_user(name,password)

        return {"Success": validate_entry, "Data": response}
