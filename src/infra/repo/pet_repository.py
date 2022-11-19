from typing import List
from src.data.interfaces import PetRepositoryInterface
from src.domain.models import Pets
from src.infra.config import DBConnectionHandler
from src.infra.entities import Pets as PetsEntity

class PetRepository(PetRepositoryInterface):
    """Class tom manage Pet Repository"""

    @classmethod
    def insert_pet(self, name: str, specie: str, age: int, user_id: int) -> Pets:
        """
        Insert data in Pet entity
        :param name: name of the pet
        :param specie: enum with species acepted
        :param age: pet age
        :param user_id: id of the owner (FK)
        :return tuple with new pet inserted
        """

        with DBConnectionHandler() as db_connection:
            try:
                new_pet = PetsEntity(name=name, specie=specie, age=age, user_id=user_id)
                db_connection.session.add(new_pet)
                db_connection.session.commit()

                return Pets(
                    id=new_pet.id,
                    name=new_pet.name,
                    specie=new_pet.specie.value,
                    age=new_pet.age,
                    user_id=new_pet.user_id
                )
            except:
                db_connection.session.rollback()
                raise
            finally:
                db_connection.session.close()

        return None

    @classmethod
    def select_pet(cls, pet_id: int = None, user_id: int = None) -> List[Pets]:
        """
        Select data in PetsEntity entity by id and/or user_id
        :param pet_id: Id of the pet registry
        :param user_id: Id of the owner
        :return: List with Pets selected
        """
        try:
            query_data = None
            filters = {}
            if pet_id:
                filters['id'] = pet_id
            if user_id:
                filters['user_id'] = user_id

            if filters:
                with DBConnectionHandler() as db_connection:
                    data = db_connection.session.query(PetsEntity).filter_by(**filters).all()
                    query_data = [data]
            return query_data
        except:
            db_connection.session.rollback()
            raise
        finally:
            if db_connection:
                db_connection.session.close()
        return None
