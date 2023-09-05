#!/usr/bin/python3

"""  Define a class """


class Rectangle:
    """
    This class defines a rectangle.

    Private instance attributes:
    - __width: Width of the rectangle.
    - __height: Height of the rectangle.

    Public class attribute:
    - number_of_instances: Ini to 0, incremented during each new instance inst,
    and decremented during each instance deletion.

    Public methods:
    - width(self): Getter method for width.
    - width(self, value): Setter method for width.
        - Width must be an integer, otherwise, raise a TypeError.
        - If width is less than 0, raise a ValueError.

    - height(self): Getter method for height.
    - height(self, value): Setter method for height.
        - Height must be an integer, otherwise, raise a TypeError.
        - If height is less than 0, raise a ValueError.

    - area(self): Returns the area of the rectangle.

    - perimeter(self): Returns the perimeter of the rectangle.
        - If width or height is equal to 0, perimeter has to be equal to 0.

    - __str__(self): Returns a string representation of the rectangle with '#
        - If width or height is equal to 0, return an empty string.

    - __repr__(self): Returns a string of the rect to be able to recreate a

    - __del__(self): Prints the  when an instance of Rectangle is deleted.

    Instantiation with optional width and height:
    - __init__(self, width=0, height=0)
    """
    number_of_instances = 0  # Class attribute

    def __init__(self, width=0, height=0):
        self.__width = 0
        self.__height = 0
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1  # Increment the instance count

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

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate and return the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return a string representation of the rectangle with '#' ."""
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle_str = ""
        for _ in range(self.__height):
            rectangle_str += "#" * self.__width + "\n"
        return rectangle_str[:-1]  # Remove the trailing newline

    def __repr__(self):
        """Return a string representation of the rectangle for eval()."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Print a message when an instance of Rectangle is deleted."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1  # Decrement the instance count
