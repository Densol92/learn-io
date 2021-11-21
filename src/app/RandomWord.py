import random


def get_random_word():
    from src import my_db
    from models.Word import Word

    from sqlalchemy import select
    stmt = select(Word)
    with my_db.Session() as session:
        x = [r for r in session.execute(stmt).scalars()]
        return random.choice(x)

# def link
