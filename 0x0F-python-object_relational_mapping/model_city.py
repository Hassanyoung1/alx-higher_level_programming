#!/usr/bin/python3

"""
model_city.py: A Python file that contains the class definition of a   City.

This module defines a SQLAlchemy model for representing states. It includes the
class `cities`, which is mapped to the 'cities' table in the database.

Classes:
    City: Represents a city with an 'id' (primary key) and 'name' column.

"""

from sqlalchemy import create_engine, Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
Base = declarative_base()


class City(Base):
    """
    The City class represents a city  with an 'id' (primary key) and 'name'
    column.

    Attributes:
        id (int): The primary key for the cities.
        name (str): The name of the cities.
        state(int): The name of the state.
    """

    __tablename__ = 'cities'
    id = Column(
        Integer,
        primary_key=True,
        nullable=False,
        unique=True,
        autoincrement=True)

    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('state.id'), nullable=False)
