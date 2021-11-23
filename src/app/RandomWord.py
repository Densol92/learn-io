import random

from models import translation, word


def get_random_word():
    from src import my_db

    from sqlalchemy import select

    stmt = select([word, translation]).select_from(word.join(translation))

    with my_db.Session() as session:
        x = [r for r in session.execute(stmt).fetchall()]
        return random.choice(x)

# def link
