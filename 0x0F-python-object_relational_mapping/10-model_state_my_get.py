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
    name = argv[4]
    Session = sessionmaker(engine)
    session = Session()

    Base.metadata.create_all(engine)
    temp = session.query(State.id).filter(
        State.name.like(name)).order_by(State.id.asc())
    num = False
    for state in temp:
        print("{}".format(state.id))
        num = True
    if num is False:
        print("Not Found")
    session.close()
