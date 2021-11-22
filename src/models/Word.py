from sqlalchemy import Column, Integer, String, Enum, Sequence
from sqlalchemy.orm import relationship

from models.Translation import Translation
from src import my_db
from src.app.Category import Category, Language


class Word(my_db.Model):
    __tablename__ = 'word'

    id = Column(Integer, Sequence('global_id_seq'), primary_key=True)
    name = Column(String, nullable=False)
    category = Column(Enum(Category), nullable=False)
    language = Column(Enum(Language), nullable=False)
    rank = Column(Integer)
    global_rank = Column(Integer)
    translations = relationship(Translation, backref='words')

