#!/usr/bin/python3
"""
Aa Python file similar to model_state.py named
 model_city.py that contains the class definition of a City.
"""
import sys
from sqlalchemy import create_engine, select
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    """ Parse command-line arguments """
    if len(sys.argv) != 4:
        print("Usage: ./script_name.py <username> <password> <database_name>")
        sys.exit(1)

    """ Create SQLAlchemy engine """
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3]
        ),
        pool_pre_ping=True
    )

    """ Create database tables """
    Base.metadata.create_all(engine)

    """ Execute select query and print results """
    with engine.connect() as conn:
        # Explicitly specify the join condition using .select_from() and
        # .join()
        s = select(
            State.name,
            City.id,
            City.name).select_from(State).join(
            City,
            State.id == City.state_id)
        result = conn.execute(s).fetchall()

        for row in result:
            print("{}: ({}) {}".format(row[0], row[1], row[2]))
