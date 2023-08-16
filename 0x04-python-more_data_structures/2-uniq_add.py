#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_int = set(my_list)
    total_result = 0
    for element in unique_int:
        if element != unique_int:
            total_result += element
    return total_result
