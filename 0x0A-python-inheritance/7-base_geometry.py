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

    def integer_validator(self, name, value):
        """
        Validate if 'value' is an integer greater than 0.

        Args:
            name (str): The name of the value being validated.
            value (int): The value to be validated.

        Raises:
            TypeError: If 'value' is not an integer.
            ValueError: If 'value' is not greater than 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
