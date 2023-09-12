#!/usr/bin/python3

""" Declare a class """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Initialize a new Rectangle instance.

    Args:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
    """
    def __init__(self, width, height):
        """
        Initialize a new Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.__width = width
        self.__height = height
        self.integer_validator("height", height)
        super().integer_validator("width", self.__width)
