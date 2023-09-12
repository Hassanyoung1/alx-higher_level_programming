#!/usr/bin/python3

"""Declare a function that returns true."""


def is_same_class(obj, a_class):
    """
    This function checks if the object 'obj' is an
    instance of the class 'a_class'.

    Args:
        obj: The object to be checked.
        a_class: The class to compare with.

    Returns:
        True if 'obj' is an instance of 'a_class', otherwise False.
    """

    if type(obj) is a_class:
        return True
    else:
        return False
