#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if value in a_dictionary.values():
        # Create a new dictionary to store non-matching key-value pairs
        new_dictionary = {}

        for key, val in a_dictionary.items():
            if val != value:
                new_dictionary[key] = val

        return new_dictionary

    return a_dictionary  # Value not found, return the original dictionary
