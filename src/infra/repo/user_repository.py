from typing import List

from src import db
from src.data.interfaces.user_repository_interface import UserRepositoryInterface
from src.domain.models import Users
from src.infra.entities import Users as UsersEntity


class UserRepository(UserRepositoryInterface):
    """Class to manage User Repository"""

    @classmethod
    def insert_user(cls, name: str, password: str) -> Users:
        """ insert data in user entity
            :param name: person name
            :param password: user password
            :return tuple with new user inserted
        """

        try:
            new_user = UsersEntity(name=name, password=password)
            db.session.add(new_user)
            db.session.commit()
            return Users(id=new_user.id,name=new_user.name, password=new_user.password)
        except:
            db.session.rollback()
            raise

    @classmethod
    def select_user(cls, user_id: int = None, name: str = None) -> List[Users]:
        """
        Select data in user entity by id and/or name
        :param user_id: Id of the registry
        :param name: User's name
        :return List with Users selected
        """
        try:
            filters = {}
            if user_id:
                filters['id'] = user_id
            if name:
                filters['name'] = name

            if filters:
                data = db.session.query(UsersEntity).filter_by(**filters).all()
            return data
        except:
            db.session.rollback()
            raise
        return None

    @classmethod
    def delete_user(cls, user_id: int) -> None:
        """ delete user register
            :param user_id: user identification
            :return None
        """

        try:
            users = cls.select_user(user_id=user_id)
            if len(users) > 0:
                db.session.delete(users[0])
                db.session.commit()
                return None
            else:
                raise Exception("User does not exist.")
        except:
            db.session.rollback()
            raise