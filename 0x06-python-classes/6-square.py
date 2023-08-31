#!/usr/bin/python3

""" Defines a square class """

class Square:
    """
    This class defines a square by its size and position.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes the square.

        Args:
            size (int): Given size of the square.
            position (tuple): Given position of the square.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """ Returns the current square size """
        return self.__size

    @size.setter
    def size(self, value):
        """ Setter for the square size """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """ Retrieves current position value """
        return self.__position

    @position.setter
    def position(self, value):
        """ Sets the value for position """
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(num, int) for num in value)
            or not all(num >= 0 for num in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ Returns the current square area """
        return self.__size * self.__size

    def my_print(self):
        """ Prints a representation of the square """
        if self.size == 0:
            print()
            return

        for _ in range(self.position[1]):
            print()

        row = ' ' * self.position[0] + '#' * self.size
        for _ in range(self.size):
            print(row)

# Example usage
if __name__ == "__main__":
    my_square = Square(4, (1, 2))
    my_square.my_print()
