#!/usr/bin/python3
"""
Python ORM Exercise
USE SQL Alchemy
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    new_entry = session.query(State).filter(State.id == 2).first()
    if new_entry:
        new_entry.name = 'New Mexico'
        session.commit()
