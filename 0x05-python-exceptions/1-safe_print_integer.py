#!/usr/bin/python3
def safe_print_integer(value):
    try:
        """ Try to format and print the value as an integer """
        print("{:d}".format(value))
        """ Print an integer succesfully """
        return True
    except ValueError:
        """ failed to print an integer (value is not an integer)"""
        return False
