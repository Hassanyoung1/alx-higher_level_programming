#!/usr/bin/python3
"""
Script that prints the State object with the name passed as an argument
from the database hbtn_0e_6_usa.
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Parse command-line arguments
    """
    if len(sys.argv) != 5:
        print("Usage: ./11-model_state_insert.py <username> <password>\
              <database_name> <state_name>")
        sys.exit(1)

    """
    Create SQLAlchemy engine
    """
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True
    )

    """
    Create session
    """
    Session = sessionmaker(bind=engine)
    session = Session()

    """
    Query the database for the State with the given name
    """
    state_name = sys.argv[4]
    result = session.query(State).filter_by(name=state_name).first()

    """
    If the state is not found, add it to the database
    """
    if not result:
        new_state = State(name=state_name)
        session.add(new_state)
        session.commit()
        print(new_state.id)
    else:
        print(result.id)
