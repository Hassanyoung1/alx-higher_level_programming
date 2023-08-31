#!/usr/bin/python3

""" Defines a square class """


class Square:
    """
    This class defines a square by its size.
    """

    def __init__(self, size=0):
        """
        Initializes the square.

        Args:
            size (int): Given size of the square.
        """
        self.size = size

    @property
    def size(self):
        """Returns the current square size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for the square size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates and returns the current square area.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size
