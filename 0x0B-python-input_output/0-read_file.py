#!/usr/bin/python3

""" Declare the function prototype """


def read_file(filename=""):
    """
    Read a text file (UTF-8 encoded) and print its content to stdout.

    :param filename: The name of the file to read (default is an empty string).
    """
    with open(filename, 'r', encoding="utf-8") as file:
        file_contents = file.read()
        print(file_contents, end="")
