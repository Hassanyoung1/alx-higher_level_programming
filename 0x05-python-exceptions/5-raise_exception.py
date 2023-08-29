#!/usr/bin/python3
def raise_exception():
    """
    Raises a type exception.
    """
    value = "string"
    try:
        result = value + 10
    except TypeError as ex:
        raise ex
