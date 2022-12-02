from abc import ABC, abstractmethod
from typing import Dict


class DeleteUser(ABC):
    """Interface to DeleteUser use case"""

    @classmethod
    @abstractmethod
    def delete(cls, user_id: int) -> Dict[bool, None]:
        """Case"""
        raise Exception("Should implement method: delete")
