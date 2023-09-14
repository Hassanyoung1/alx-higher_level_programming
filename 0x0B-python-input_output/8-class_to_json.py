#!/usr/bin/python3

"""Defines class_to_json function."""


def class_to_json(obj):
    """
    Return a dictionary representation of the object.

    :param obj: The object to be converted into a dictionary.
    :return: A dictionary representing the object's attributes.
    """
    return obj.__dict__
