#!/usr/bin/python3

""" Import module """
import json

""" Declare function prototype """


def save_to_json_file(my_obj, filename):
    """
    Serialize an object to its JSON representation and save it to a text file.

    :param my_obj: The Python object to be serialized.
    :param filename: The name of the file to save the JSON representation to.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
