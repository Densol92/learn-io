from sqlalchemy import Column, ForeignKey, Float, Integer, Sequence

from src import my_db


class Translation(my_db.Model):
    __tablename__ = 'translation'
    id = Column(Integer, Sequence('global_id_seq'), primary_key=True)
    word = Column('word_id', ForeignKey('word.id'))
    translation = Column(ForeignKey('word.id'))
    popularity = Column(Float)

    # translations_it = relationship(Word, backref="translations")
    # word_it = relationship(Word, backref="translations")
