#!/usr/bin/python3

""" import modules """
import json

""" Declare function prototype """


def load_from_json_file(filename):
    """
    Load an object from a JSON file.

    :param filename: The name of the JSON file to load the object from.
    :return: The loaded Python object.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
