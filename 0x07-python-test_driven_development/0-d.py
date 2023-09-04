#!/usr/bin/python3

"""
    function to add two integers
    Arg: a and b
    Return: a + b
"""


def add_integer(a, b=98):
    """ Adds two numbers and returns the result as an integer
        Return: int(a + b)
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
