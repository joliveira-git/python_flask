from faker import Faker

from src.data.register_user import RegisterUser
from src.infra.test import UserRepositorySpy

faker = Faker()

def test_register():
    """Testing registry method"""

    user_repo = UserRepositorySpy()
    register_user = RegisterUser(user_repo)

    attributes = {
        "name": faker.name(),
        "password": faker.name()
    }

    response = register_user.register(name=attributes["name"], password=attributes["password"])

    assert user_repo.insert_user_params["name"] == attributes["name"]
    assert user_repo.insert_user_params["password"] == attributes["password"]

    assert response["Success"] is True
    assert response["Data"]

def test_register_fail():
    """Testing registry method fail"""

    user_repo = UserRepositorySpy()
    register_user = RegisterUser(user_repo)

    attributes = {
        "name": faker.random_number(digits=2),
        "password": faker.name()
    }

    response = register_user.register(name=attributes["name"], password=attributes["password"])

    assert user_repo.insert_user_params == {}

    assert response["Success"] is False
    assert response["Data"] is None