import random


def get_random_word():
    from src import my_db, m

    from sqlalchemy import select
    stmt = select(m.Word)
    with my_db.Session() as session:
        return random.choice([r for r in session.execute(stmt).scalars()])
