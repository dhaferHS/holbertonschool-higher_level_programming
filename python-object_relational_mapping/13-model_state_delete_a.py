#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from sqlalchemy.orm import Session
import model_state
from model_state import Base, State
from sqlalchemy import create_engine

if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            user, password, database),
        pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    deletes = session.query(State).order_by(State.id).all()
    for row in deletes:
        if 'a' in row.name:
            session.delete(row)
    session.commit()
    session.close()
