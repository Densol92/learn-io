from sqla_wrapper import SQLAlchemy

from .config import DATABASE_URI

my_db: SQLAlchemy = SQLAlchemy(DATABASE_URI)
from . import models as m  # noqa

