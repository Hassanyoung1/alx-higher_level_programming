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

    print_int = 0

    for num in range(0, x):
        try:
            print("{:d}".format(my_list[num]), end="")
            print_int += 1
        except (ValueError, TypeError):
            pass
    print()
    return print_int
