#!/usr/bin/python3

""" importing from base  """


from models.base import Base

""" Declare Class """


class Rectangle(Base):
    """
    Represents a rectangle.

    This class inherits from the Base class
    and defines a rectangle with
    attributes for width, height, x-coordinate,
     y-coordinate, and an ID.

    Attributes:
        id (int): The identifier for the rectangle.
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        x (int): The x-coordinate of the upper-left corner.
        y (int): The y-coordinate of the upper-left corner.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a new Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate of the
                upper-left corner (default is 0).
            y (int, optional): The y-coordinate of the
                upper-left corner (default is 0).
            id (int, optional): The identifier for the
                rectangle (default is None).
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        """
        Calculate and return the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.height * self.width

    def display(self):
        """
        Display the rectangle by printing it to stdout.

        This method prints the rectangle using '#' characters,
        with the upper-left corner offset by the 'x' and 'y'
        attributes.
        """
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """
        Return a string representation of the rectangle.

        Returns:
            str: A string representing the rectangle in the format:
                 "[Rectangle] (id) x/y - width/height".
        """
        f = f"[Rectangle] ({self.id}) "
        a = f"{self.x}/{self.y} - {self.width}/{self.height}"
        return f + a

    def update(self, *args, **kwargs):
        """
        Update the attributes of the rectangle.

        This method can update the attributes of the rectangle
        using either positional arguments or keyword arguments.

        Args:
            *args: Positional arguments for updating attributes
                in the order: (id, width, height, x, y).
            **kwargs: Keyword arguments for updating attributes
                by name.

        Example:
            rect.update(1, 10, 20)  # Updates id, width, and height
            rect.update(x=5, y=5)   # Updates x and y coordinates
        """
        if len(args) > 0:
            selfs = ["id", 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, selfs[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Convert the rectangle attributes to a dictionary.

        Returns:
            dict: A dictionary containing the rectangle's attributes.
                Keys: 'id', 'width', 'height', 'x', 'y'.
        """
        return {
                'id': self.id,
                'width': self.width,
                'height': self.height,
                'x': self.x,
                'y': self.y
                }

    @property
    def width(self):
        """
        Getter method for the width attribute.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for the width attribute.

        Args:
            value (int): The new width value.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is not greater than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("Width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter method for the height attribute.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method for the height attribute.

        Args:
            value (int): The new height value.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is not greater than 0.
        """
        if not isinstance(value, int):
            raise TypeError("Height must be an integer")
        if value <= 0:
            raise ValueError("Height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        Getter method for the x-coordinate attribute.

        Returns:
            int: The x-coordinate of the upper-left corner.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is negative.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter method for the x-coordinate attribute.

        Args:
            value (int): The new x-coordinate value.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Getter method for the y-coordinate attribute.

        Returns:
            int: The y-coordinate of the upper-left corner.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is negative.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter method for the y-coordinate attribute.

        Args:
            value (int): The new y-coordinate value.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
