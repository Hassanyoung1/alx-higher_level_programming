#!/usr/bin/python3

"""
5-text_indentation module

This module contains a function for text indentation.
"""


def text_indentation(text):
    """
    Formats the given text by adding two new lines after '.', '
    ?', and ':' characters.

    Args:
        text (str): The input text to be formatted.

    Raises:
        TypeError: If the input 'text' is not a string.

    Returns:
        None: This function does not return a value.
        It prints the formatted text.

    """
    """ Check if the input is a string """
    if not isinstance(text, str):
        """ Raise TypeError if the input 'text' is not a string """
        raise TypeError("text must be a string")

    """ Initialize an empty result string """
    result = ""

    """ Flag to track if a newline has been added recently """
    new_line_added = True

    """ Iterate through each character in the input text """
    for char in text:
        """ Add the character to the result string """
        result += char

        """ Check if the char is one of the specified punctuation marks """
        if char in (".", "?", ":"):
            """ Add two newlines after the punctuation """
            result += "\n\n"
            new_line_added = True
        else:
            new_line_added = False

    """ Split the result into lines """
    lines = result.splitlines()

    """ Remove leading and trailing whitespaces from each line """
    trimmed_lines = [line.strip() for line in lines]

    """ Join the lines to form the final formatted text """
    formatted_text = "\n".join(trimmed_lines)

    """ Print the formatted text """
    print(formatted_text)
