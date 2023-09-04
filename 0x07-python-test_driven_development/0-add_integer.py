#!/usr/bin/python3

"""
Define add_integer function
Takes 2 arguments (a and b)
Returns: a + b
"""


def add_integer(a, b=98):
    """
    Add 2 integers
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    elif type(b) not in (int, float):
        raise TypeError("b must be an integer")
    return int(a + b)
