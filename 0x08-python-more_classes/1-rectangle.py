#!/usr/bin/python3

"""" Define an class triangle """

class Rectangle:
    def __init__(self, width=0, height=0):
        self.__width = 0
        self.__height = 0


    def width(self):
        return self.__width

    @proprtysetter
    def width(self, value):
        self.__value = value
        if not isinstance(value, int):
            raise ValueError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")

    def height(self):
        return self.__height

    def height(self, value):
        self.__value = value
        if not isinstance(value, int):
            raise ValueError("height must be an integer")
        if



