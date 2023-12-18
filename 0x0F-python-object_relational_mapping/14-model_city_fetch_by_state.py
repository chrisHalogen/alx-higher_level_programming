#!/usr/bin/python3
"""
Python ORM Exercise
USE SQL Alchemy 7 - 14
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    q = session.query(State, City).filter(State.id == City.state_id).all()
    for state, city in q:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
