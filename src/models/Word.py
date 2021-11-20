from sqlalchemy import Column, Integer, String, Enum, Sequence

from ..app.Category import Category
from .. import db


class Word(db.Model):
    __tablename__ = 'word'

    id = Column(Integer, Sequence('global_id_seq'), primary_key=True)
    name = Column(String, nullable=False)
    category = Column(Enum(Category), nullable=False)
    rank = Column(Integer)
    global_rank = Column(Integer)
