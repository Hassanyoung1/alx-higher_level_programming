#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    unique_elements = set()

    for element in set_1:
        if element not in set_2:
            unique_elements.add(element)

    for element in set_2:
        if element not in set_1:
            unique_elements.add(element)

    return unique_elements
