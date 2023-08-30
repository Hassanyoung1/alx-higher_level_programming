class Square:
    """
    This class defines a square by its size.
    """

    def __init__(self, size=0):
        """
        Initializes a Square instance with an optional size.

        Args:
            size (int): The size of the square. Defaults to 0.
                Must be a positive integer.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
