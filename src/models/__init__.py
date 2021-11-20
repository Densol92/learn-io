from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

engine = create_engine('sqlite:////home/densolovev/Projects/learn-io/learn-io.db', echo=True)
Base = declarative_base()

