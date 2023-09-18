#!/usr/bin/python3

""" Import modules """

from models.rectangle import Rectangle

""" Declare Classes """


class Square(Rectangle):

    """A class representing a square, derived from Rectangle.

    Args:
        size (int): The size of the square.
        x (int, optional): The x-coordinate of
        the square's position. Defaults to 0.
        y (int, optional): The y-coordinate of the
        square's position. Defaults to 0.
        id (int, optional): The unique identifier of
        the square. Defaults to None.

    Attributes:
        size (int): The size of the square.
        x (int): The x-coordinate of the square's position.
        y (int): The y-coordinate of the square's position.
        id (int): The unique identifier of the square.

    Methods:
        __str__(): Returns a string representation of the square.
        update(*args, **kwargs): Updates the square's attributes
        using either positional arguments or keyword arguments.
        to_dictionary(): Returns a dictionary representation of the square.

    Note:
        The Square class inherits from the Rectangle class and
        ensures that both the width and height are equal,
        as it represents a square.
    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        a = f"[{__class__.__name__}] ({self.id}) "
        b = f"{self.x}/{self.y} - {self.width}"
        return a + b

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        if len(args) > 0:
            arg = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                setattr(self, arg[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        return {
                'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y
                }
