#!/usr/bin/python3


""" Declare the function """


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text after each line
    containing a specific string in a file.

    Args:
        filename (str): The name of the file to modify.
        search_string (str): The string to search for in each line.
        new_string (str): The line of text to insert
        after lines containing the search string.
    """
    # Check if any of the arguments are empty
    if filename == "" or search_string == "" or new_string == "":
        return

    # Create a list to hold the modified lines
    line_text = []

    # Open the file for reading
    with open(filename, 'r', encoding="utf-8") as file:
        for line in file:
            line_text.append(line)
            if search_string in line:
                line_text.append(new_string)

    # Write the modified lines back to the file
    with open(filename, 'w', encoding="utf-8") as file:
        file.writelines(line_text)
