#!/usr/bin/python3
"""
Module 9-square
Defines a square based on 9-rectangle.py
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Represents a square.
    Private instance attribute: __size
    """

    def __init__(self, size):
        """
        Initializes a new Square instance.
        Args:
            size (int): The size of the square's side.
        """
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """
        Computes the area of the square.
        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def __str__(self):
        """
        Returns a string representation of the square.
        """
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
