#!/usr/bin/python3

""" Declare a function prototype """


def append_write(filename="", text=""):
    """
    Append text to a file with the specified filename.

    :param filename: The name of the file to append to
    (default is an empty string).
    :param text: The text to be append to the file
    (default is an empty string).
    """
    with open(filename, "a", encoding="utf-8") as file:
        file_content = file.write(text)
        return file_content
