from typing import List

from src.domain.models import Pets


class PetsSerializer:

    @staticmethod
    def serializer(pets: List[Pets]):
        result = []
        for pet in pets:
            # TODO: revisar este código VVVV
            result.append(
                {
                    "type": "pets",
                    "id": pet.id,
                    "attributest": {"name": pet.name},
                }
            )
        return result