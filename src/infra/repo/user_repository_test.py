from faker import Faker
from src.infra.config import DBConnectionHandler
from .user_repository import UserRepository
from src.infra.entities import Users


faker = Faker()
user_repository = UserRepository()
db_connection_handler = DBConnectionHandler()

def test_insert_user():
    """Should insert user"""
    name = faker.name()
    password = faker.word()
    engine = db_connection_handler.get_engine()

    new_user = user_repository.insert_user(name, password)
    user = engine.execute("SELECT * FROM users WHERE id='{}';".format(new_user.id)).fetchone()

    engine.execute("DELETE FROM users WHERE id='{}'".format(new_user.id))

    assert new_user.id == user.id
    assert new_user.name == user.name
    assert new_user.password == user.password


def test_select_user():
    """Shoul select a user in Users table and compare it"""

    user_id = faker.random_number(digits=5)
    name = faker.name()
    password = faker.word()
    data = Users(id=user_id, name=name, password=password)

    engine = db_connection_handler.get_engine()
    engine.execute("INSERT INTO users (id, name, password) VALUES ('{}','{}','{}');".format(user_id, name, password))

    users1 = user_repository.select_user(user_id=user_id)
    users2 = user_repository.select_user(name=name)
    users3 = user_repository.select_user(user_id=user_id, name=name)

    assert data in users1[0]
    assert data in users2[0]
    assert data in users3[0]

    engine.execute("DELETE FROM users WHERE id='{}';".format(user_id))
