from faker import Faker
from .user_repository import userRepository
from src.infra.config import DBConnectionHandler

faker = Faker()
user_repository = userRepository()
db_connection_handler = DBConnectionHandler()

def test_insert_user():
    """Should insert user"""
    name = faker.name()
    password = faker.word()
    engine = db_connection_handler.get_engine()

    new_user = user_repository.insert_user(name, password)
    user = engine.execute("SELECT * FROM users WHERE id='{}';".format(new_user.id)).fetchone()
    assert new_user.id == user.id
    assert new_user.name == user.name
    assert new_user.password == user.password
    engine.execute("DELETE FROM users WHERE id='{}'".format(new_user.id))
