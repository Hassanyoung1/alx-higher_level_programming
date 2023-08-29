#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """
    Print the first x integers from the list my_list.

    Args:
        my_list (list): List containing elements of any type.
        x (int): Number of elements to access in my_list.

    Returns:
        int: The real number of integers printed.
    """
    printed_integers = 0  # To keep track of the number of integers printed
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            printed_integers += 1
        except (TypeError, ValueError):
            pass
        print()  # Print a new line after printing the integers
        return printed_integers
