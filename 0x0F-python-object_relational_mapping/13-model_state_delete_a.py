#!/usr/bin/python3
"""
a script that deletes all State objects with a name containing the
letter a from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine, delete
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

    delete_state = delete(State).where(State.name.like('%a%'))
    session.execute(delete_state)
    session.commit()

    session.close()
