   #!/usr/bin/python3

""" Defines a square class """


class Square:
    """ This is an empty square class """

    def __init__(self, size=0, position=(0, 0)):
        """ Initializes the square
        Args:
            size (int): Given size of the square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """ Returns the current square size """
        return self.__size

    @size.setter
    def size(self, value):
        """ setter for the square size"""
        try:
            if not isinstance(value, int):
                raise TypeError
        except (TypeError, ValueError):
            raise TypeError("size must be an integer")
        else:
            self.__size = value
            if self.__size < 0:
                raise ValueError("size must be >= 0")

    @property
    def position(self):
        """ retrieves current position value"""
        return self.__position

    @position.setter
    def position(self, value):
        """ sets the value for position"""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """ Returns the current square area """
        return self.__size * self.__size

    def my_print(self):
        """Prints a representation of the square."""
        if self.size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()

        row = ' ' * self.__position[0] + '#' * self.size
        for _ in range(self.size):
            print(row)
