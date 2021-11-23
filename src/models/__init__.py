from sqlalchemy import Table, Column, Integer, String, Enum, Sequence, ForeignKey

from src.app.Category import Category, Language
from src import my_db

word = Table('word', my_db.registry.metadata,
             Column("id", Integer, Sequence('global_id_seq'), primary_key=True),
             Column("name", String, nullable=False),
             Column("category", Enum(Category), nullable=False),
             Column("language", Enum(Language), nullable=True),
             Column("rank", Integer),
             Column("global_rank", Integer)
             # relationship("translations",Translation, backref='words')
             )

translation = Table(
    "translation", my_db.registry.metadata,
    Column('id', Integer, Sequence('global_id_seq'), primary_key=True),
    Column('word_id', ForeignKey('word.id')),
    Column("translation", String, nullable=False),
)
