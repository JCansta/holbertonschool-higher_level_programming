#!/usr/bin/python3
"""
    print database with filters
"""
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Session = sessionmaker(engine)
    session = Session()
    Base.metadata.create_all(engine)
    new = State(name="California", cities=[City(name="San Francisco")])
    session.add(new)
    session.commit()
    session.close()
