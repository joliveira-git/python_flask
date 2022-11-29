from typing import List

from src.domain.models import Pets


class PetsSerializer:

    @staticmethod
    def serializer(pets: List[Pets]):
        result = []
        for pet in pets:
            result.append(
                {
                    "type": "pets",
                    "id": pet.id,
                    "attributest": {"name": pet.name,
                                    "specie": pet.specie,
                                    "age": pet.age,
                                    "user_id": pet.user_id},
                }
            )
        return result