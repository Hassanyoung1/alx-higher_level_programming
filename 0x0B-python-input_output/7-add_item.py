#!/usr/bin/python3

"""
A script that appends command-line arguments to a JSON file.

Usage:
    python3 script_name.py arg1 arg2 ...

The script reads an existing JSON file, if it exists, and appends the provided
command-line arguments to it. The updated JSON data is then saved back to the
file.
"""

from sys import argv
from os.path import exists

if __name__ == "__main__":
    # Import the necessary functions from external modules
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
            __import__('6-load_from_json_file').load_from_json_file

    my_list = []

    try:
        # Load existing JSON data from a file, if it exists
        my_list = load_from_json_file("add_item.json")
    except Exception:
        pass

    # Check if command-line arguments are provided
    if len(argv) > 1:
        # Append command-line arguments to the list
        for num in range(1, len(argv)):
            my_list.append(argv[num])

    # Save the updated list to a JSON file
    save_to_json_file(my_list, "add_item.json")
