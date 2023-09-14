#!/usr/bin/python3
"""" import module """

import json

""" Declare function prototype """


def from_json_string(my_str):
    """
    Convert a JSON-formatted string to a Python object.

    :param my_str: A JSON-formatted string to be converted to a
    Python object.
    :return: A Python object created from the JSON string.
    """
    return json.loads(my_str)
