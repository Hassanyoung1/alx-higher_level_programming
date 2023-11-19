#!/usr/bin/python3

"""
model_state.py: A Python file that contains the class definition of a State.

This module defines a SQLAlchemy model for representing states. It includes the
class `State`, which is mapped to the 'states' table in the database.

Classes:
    State: Represents a state with an 'id' (primary key) and 'name' column.

"""

from sqlalchemy import create_engine, Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    The State class represents a state with an 'id' (primary key) and 'name'
    column.

    Attributes:
        id (int): The primary key for the state.
        name (str): The name of the state.
    """

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128))
