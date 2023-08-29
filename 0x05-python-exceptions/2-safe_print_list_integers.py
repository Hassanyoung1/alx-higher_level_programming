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

    try:
        for item in my_list:
            if printed_integers == x:  # Stop printing when required number of integers are printed
                break

            try:
                formatted_value = "{:d}".format(item)
                print(formatted_value, end="")  # Print the formatted value on the same line
                printed_integers += 1
            except (TypeError, ValueError):
                pass  # If the item is not an integer, silently skip it

        print()  # Print a new line after printing the integers
        return printed_integers
    except IndexError:
        return printed_integers  # Return the count of printed integers even if an exception occurred
