#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    sorted_key = sorted(a_dictionary.keys())
    for key in sorted_key:
        print(f"{key}: {a_dictionary[key]}")
