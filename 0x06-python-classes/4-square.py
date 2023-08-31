#!/usr/bin/python3

""" Defines a square class """


class Square:

    """
    This class defines a square by its size.
    """

    def __init__(self, size=0):
        """Initializes the square.

        Args:
            size (int): Given size of the square.
        """

        self.size = size
        @propertY
        def size(self):
              """ Returns the current square size """
            return self.__size

        @size.setter
        def size(self, value):
            """ setter for the square size """
        try:
            if not isinstance(size, int):
                raise TypeError
        except (TypeError, ValueError):
            raise TypeError("size must be an integer")
        else:
            self.__size = size
            if self.__size < 0:
                raise ValueError("size must be >= 0")

    def area(self):
        """Calculates and returns the current square area.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size
