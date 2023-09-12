#!/usr/bin/python3

""" Delare function inherit_from """


def inherits_from(obj, a_class):
    """
    Check if the object 'obj' is an instance of a class that
    inherits from 'a_class'.

    Args:
        obj: The object to be checked.
        a_class: The class to compare with.

    Returns:
        True if 'obj' is an instance of a class that inherits from
        'a_class', otherwise False.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
