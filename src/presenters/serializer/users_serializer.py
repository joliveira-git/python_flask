from typing import List

from src.domain.models import Users


class UsersSerializer:

    @staticmethod
    def serializer(users: List[Users]):
        result = []
        for user in users:
            result.append(
                {
                    "type": "users",
                    "id": user.id,
                    "attributes": {"name": user.name},
                }
            )
        return result