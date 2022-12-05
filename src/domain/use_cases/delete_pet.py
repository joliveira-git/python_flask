from abc import ABC, abstractmethod
from typing import Dict


class DeletePet(ABC):
    """Interface to DeletePet use case"""

    @classmethod
    @abstractmethod
    def delete(cls, pet_id: int) -> Dict[bool, None]:
        """Case"""
        raise Exception("Should implement method: delete")
