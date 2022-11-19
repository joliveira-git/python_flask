from abc import ABC
from typing import Dict, List

from src.domain.models import Pets


class FindPet(ABC):
    """Interface to FindPet use case"""

    @classmethod
    def by_pet_id(cls, pet_id: int) -> Dict[bool, List[Pets]]:
        """Specific Case"""
        raise Exception("Should implements method: by_pet_id")

    @classmethod
    def by_user_id(cls, user_id: int) -> Dict[bool, List[Pets]]:
        """Specific Case"""
        raise Exception("Should implements method: by_name")

    @classmethod
    def by_pet_id_and_user_id(cls, pet_id: int, user_id: int) -> Dict[bool, List[Pets]]:
        """Specific Case"""
        raise Exception("Should implements method: by_name")