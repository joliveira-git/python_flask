from src import db

Column = db.Column
Model = db.Model
class Users(Model):
    """Users Entity"""

    __tablename__ = "users"

    id = Column(db.Integer, primary_key=True)
    name = Column(db.String, nullable=False, unique=True)
    password = Column(db.String, nullable=False)
    id_pet = db.relationship("Pets")

    def __repr__(self):
        return f"Usr [name={self.name}"

    def __eq__(self, other):
        if (
                self.id == other.id
                and self.name == other.name
                and self.password == other.password
        ):
            return True
        return False