#!/usr/bin/python3
"""
    print database with filters
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Session = sessionmaker(engine)
    session = Session()

    new = State(name='Louisiana')
    session.add(new)
    session.commit()
    Base.metadata.create_all(engine)
    temp = session.query(State.id).order_by(State.id.desc()).limit(1)
    for state in temp:
        print(state.id)
    session.close()
