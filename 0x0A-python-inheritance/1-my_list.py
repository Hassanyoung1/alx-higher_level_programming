#!/usr/bin/python3

""" Declare a class """

class MyList(list):
    """
    A custom list class that inherits from the built-in list class.
    This class provides an additional method for printing the list in ascending order.

    Attributes:
        Inherits all attributes and methods from the list class.

    Methods:
        print_sorted(): Prints the list in ascending order.
    """

    def print_sorted(self):
        """
        Print the list in ascending order.

        Usage:
            my_list.print_sorted()  # Prints the list in ascending order.
        """
        sorted_list = sorted(self)
        print(sorted_list)
