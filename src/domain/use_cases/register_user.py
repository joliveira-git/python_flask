from abc import ABC, abstractmethod
from typing import Dict

from src.domain.models import Users

class RegisterUser(ABC):
    """Interface to RegisterUser use case"""

    @classmethod
    @abstractmethod
    def register(cls, name, str, password: str) -> Dict[bool, Users]:
        """Case"""
        raise Exception("Should implement method: register")
