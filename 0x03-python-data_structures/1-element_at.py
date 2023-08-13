#!/usr/bin/python3
def element_at(my_list, idx):
    for idx in my_list:
        if idx < 0:
            return None
        if idx >= len(my_list):
            return None
        else:
            return my_list[idx]
