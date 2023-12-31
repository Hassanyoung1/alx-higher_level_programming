#!/usr/bin/python3

""" Declare a class """


class BaseGeometry:
    """
    This is the BaseGeometry class docstring.
    You can provide information about the class and its purpose here.
    """

    def area(self):
        """
        This method is not implemented in the BaseGeometry class.
        Subclasses should override this method to calculate the area.
        """
        raise Exception("area() is not implemented")
