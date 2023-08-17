#!/usr/bin/python3
def common_elements(set_1, set_2):
    common_set = set()  # Create a new set to store the common elements
    
    for element in set_1:
        if element in set_2:
            common_set.add(element)  # Add element if it's in both sets
    
    return common_set
