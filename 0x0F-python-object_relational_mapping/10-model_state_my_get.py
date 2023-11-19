#!/usr/bin/python3

"""
a script that lists all State objects that
contain the letter a from the database
 use the module SQLAlchemy
"""
import sys
from model_state import Base, State

from sqlalchemy import (create_engine)
from sqlalchemy.sql import select

if __name__ == "__main__":

    """ Parse command-line arguments """
    if len(sys.argv) != 5:
        print("Usage: ./7-model_state_fetch_all.py <username> <password>\
                <database_name>")
        sys.exit(1)

    """ Create SQLAlchemy engine """
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3]),
        pool_pre_ping=True)

    """  Create database tables """
    Base.metadata.create_all(engine)

    """ Execute select query and print results """
    with engine.connect() as conn:
        s = select(State).where(State.name == sys.argv[4])
        result = conn.execute(s).first()
        if result:
            print("{}".format(result[0]))
        else:
            print("Not found")
