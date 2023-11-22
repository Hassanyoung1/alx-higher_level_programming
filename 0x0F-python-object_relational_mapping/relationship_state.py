#!/usr/bin/python3

"""
model_state.py: A Python file that contains the class definition of a State.

This module defines a SQLAlchemy model for representing states. It includes the
class `State`, which is mapped to the 'states' table in the database.

Classes:
    State: Represents a state with an 'id' (primary key) and 'name' column.

"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)

    # Import City class after its definition
    from relationship_city import City

    # Define the relationship with the City class
    cities = relationship('City', backref='state', cascade='all, delete-orphan')


