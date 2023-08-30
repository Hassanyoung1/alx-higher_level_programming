#!/usr/bin/python3

"""
This is an empty square class
"""

class Square:
    """This is an empty square class"""

    def __init__(self, size=0):
        """Initializes the square
        Args:
            size (int): Given size of the square
        """
        self.__size = size
        if self.__size < 0:
            raise ValueError("size must be >= 0")
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
