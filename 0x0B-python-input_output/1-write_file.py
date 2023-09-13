#!/usr/bin/python3

""" Declare a function prototype """


def write_file(filename="", text=""):
    """
    Write text to a file with the specified filename.

    :param filename: The name of the file to write to
    (default is an empty string).
    :param text: The text to be written to the file
    (default is an empty string).
    """
    with open(filename, "w", encoding="utf-8") as file:
        file_content = file.write(text)
        return file_content
