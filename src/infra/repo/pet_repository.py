from typing import List

from src import db
from src.data.interfaces import PetRepositoryInterface
from src.domain.models import Pets
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

        try:
            new_pet = PetsEntity(name=name, specie=specie, age=age, user_id=user_id)
            db.session.add(new_pet)
            db.session.commit()

            return Pets(
                id=new_pet.id,
                name=new_pet.name,
                specie=new_pet.specie.value,
                age=new_pet.age,
                user_id=new_pet.user_id
            )
        except:
            db.session.rollback()
            raise

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
                data = db.session.query(PetsEntity).filter_by(**filters).all()
            return data
        except:
            db.session.rollback()
            raise
        return None

    @classmethod
    def delete_pet(cls, pet_id: int) -> None:
        """ delete pet registers
            :param pet_id: pet identification
            :return None
        """

        try:
            pets = cls.select_pet(pet_id=pet_id)
            if len(pets) > 0:
                db.session.delete(pets[0])
                db.session.commit()
                return None
            else:
                raise Exception("Pet does not exist.")
        except:
            db.session.rollback()
            raise
