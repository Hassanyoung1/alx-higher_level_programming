#!/usr/bin/python3

"""" Define an class triangle """


class Rectangle:
    """
    Define a class Rectangle.

    Private instance attributes:
    - __width: Width of the rectangle.
    - __height: Height of the rectangle.

    Public methods:
    - width(self): Getter method for width.
    - width(self, value): Setter method for width.
    - height(self): Getter method for height.
    - height(self, value): Setter method for height.

    Instantiation with optional width and height:
    - __init__(self, width=0, height=0)
    """

    def __init__(self, width=0, height=0):
        self.__width = 0
        self.__height = 0
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
