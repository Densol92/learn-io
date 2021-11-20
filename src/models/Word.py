from sqlalchemy import Column, Integer, String, Enum, Sequence

from models import Base


class Word(Base):
    __tablename__ = 'word'

    id = Column(Integer, Sequence('global_id_seq'), primary_key=True)
    name = Column(String)
    category = Column(Enum)
    rank = Column(Integer)
    global_rank = Column(Integer)
