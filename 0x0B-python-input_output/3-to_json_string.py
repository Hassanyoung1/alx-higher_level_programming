#!/usr/bin/python3

"""" Declare function prototype """


import json


def to_json_string(my_obj):
    """
    Convert a Python object to its JSON representation as a string.

    :param my_obj: The Python object to be converted to JSON.
    :return: A JSON-formatted string representing the Python object.
    """
    return json.dumps(my_obj)
