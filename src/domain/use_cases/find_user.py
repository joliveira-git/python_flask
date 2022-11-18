from abc import ABC, abstractclassmethod, abstractmethod
from typing import Dict, List
from src.domain.models import Users

class FindUser(ABC):
    """Interface to FindPet use case"""

    @classmethod
    def by_id(cls, user_id: int) -> Dict[bool, List[Users]]:
        """Specific Case"""
        raise Exception("Should implements method: by_id")

    @classmethod
    def by_name(cls, name: str) -> Dict[bool, List[Users]]:
        """Specific Case"""
        raise Exception("Should implements method: by_name")

    @classmethod
    def by_id_and_name(cls, user_id: int, name: str) -> Dict[bool, List[Users]]:
        """Specific Case"""
        raise Exception("Should implements method: by_name")