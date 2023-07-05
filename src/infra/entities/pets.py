from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from src.infra.config import Base
import enum


class AnymalTypes(enum.Enum):
    """Derfining Anymals Types"""
    dog = "dog"
    cat = "cat"
    fish = "fish"
    turtle = "turtle"


class Pets(Base):
    "Pets entity"

    __tablename__ = "pets"
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False, unique=True)
    specie = Column(Enum(AnymalTypes), nullable=False)
    age = Column(Integer)
    user_id = Column(Integer, ForeignKey("users.id"))

    def __repr__(self):
        return f"Pet: [name={self.name}]"
