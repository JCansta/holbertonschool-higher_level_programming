#!/usr/bin/python3
"""
    print database with filters
"""
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Session = sessionmaker(engine)
    session = Session()
    Base.metadata.create_all(engine)
    for state, city in session.query(State, City).join(City).order_by(City.id):
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
