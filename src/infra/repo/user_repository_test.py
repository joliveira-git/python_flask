from faker import Faker

from src.infra.entities import Users
from .user_repository import UserRepository
from ..test.base_test import BaseTest
from ... import db

faker = Faker()
class TestUserRepository(BaseTest):

    @classmethod
    def setup_class(cls):
        cls.user_repository = UserRepository()

    def test_insert_user(self):
        """Should insert user"""
        name = faker.name()
        password = faker.word()

        new_user = self.user_repository.insert_user(name, password)

        user = db.session.query(Users).filter(Users.id == new_user.id).first()

        assert new_user.id == user.id
        assert new_user.name == user.name
        assert new_user.password == user.password


    def test_select_user(self):
        """Shoul select a user in Users table and compare it"""

        name = faker.name()
        password = faker.word()

        new_user = self.user_repository.insert_user(name, password)

        users1 = self.user_repository.select_user(user_id=new_user.id)
        users2 = self.user_repository.select_user(name=new_user.name)
        users3 = self.user_repository.select_user(user_id=new_user.id, name=new_user.name)

        assert len(users1)
        assert len(users2)
        assert len(users3)
