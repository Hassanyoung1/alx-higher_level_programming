#!/usr/bin/python3

""" function that returns list of available attributes and methods of an obj"""


def lookup(obj):
    """
    Return the list of available attribute and methods of an object

    Arg:
       object to inspect
    Return:
        list object to be return
    """
    return dir(obj)
