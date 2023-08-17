#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    common_set = set()

    for element in set_1:
        if element != set_2:
            common_set.add(element)
    for element in set_2:
        if element != set_1:
            common_set.add(element)
        return common_set
