from sqla_wrapper import SQLAlchemy

from .config import DATABASE_URI


db: SQLAlchemy = SQLAlchemy(DATABASE_URI)
from src import models  # noqa
