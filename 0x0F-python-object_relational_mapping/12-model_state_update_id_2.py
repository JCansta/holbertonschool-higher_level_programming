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

    upd = session.query(State).filter(State.id.like(2)).first()
    upd.name = 'New Mexico'
    session.add(upd)
    session.commit()
    session.close()
