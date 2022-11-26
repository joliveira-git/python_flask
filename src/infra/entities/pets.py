import enum

from sqlalchemy import ForeignKey, Enum

from src import db

Column = db.Column
Model = db.Model
class AnimalTypes(enum.Enum):
    """Defining Animals types"""

    dog = "dog"
    cat = "cat"
    fish = "fish"
    turtle = "turtle"


class Pets(Model):
    """Pets Entity"""

    __tablename__ = "pets"

    id = Column(db.Integer, primary_key=True)
    name = Column(db.String(20), nullable=False, unique=True)
    specie = Column(Enum(AnimalTypes), nullable=False)
    age = Column(db.Integer)
    user_id = Column(db.Integer, ForeignKey("users.id"))

    def __repr__(self):
        return f"Pet: [name={self.name}, specie={self.specie}, user_id={self.user_id}"

    def __eq__(self, other):
        if (
                self.id == other.id
                and self.name == other.name
                and self.specie == other.specie
                and self.age == other.age
                and self.user_id == other.user_id):
            return True
        return False
