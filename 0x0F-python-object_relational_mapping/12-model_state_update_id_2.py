#!/usr/bin/python3
"""
This script adds the State object “Louisiana” to the database hbtn_0e_6_usa
It takes 3 arguments: mysql username, mysql password, and database name.
"""

import sys
from sqlalchemy import create_engine, update
from sqlalchemy.orm import Session
from model_state import Base, State

if __name__ == "__main__":
    """ Check if the number of arguments is correct """
    if len(sys.argv) != 4:
        print('Usage: argv[0] <username> <password> <database>',
              file=sys.stderr)
        exit()

    """ Create a SQLAlchemy engine that provides a source of database
     connectivity """
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1],  # username
            sys.argv[2],  # password
            sys.argv[3]   # database name
        ),
        pool_pre_ping=True
    )

    """ Create all tables in the engine ("Base.metadata.create_all" is akin to
     "CREATE TABLE" statement in raw SQL)"""
    Base.metadata.create_all(engine)

    """ Create a new sessionn """
    session = Session(engine)

    update_state = update(State).where(State.id == 2).values(name="New Mexico")
    session.execute(update_state)
    session.commit()

    session.close()
