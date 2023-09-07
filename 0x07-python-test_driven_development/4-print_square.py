#!/usr/bin/python3
""" Declare print square """


def print_square(size):
    """
    Prints a square of size 'size' with '#' character.

    Args:
        size (int): The size of the square's side.

    Raises:
        TypeError: If size is not an integer or is less than 0,
        with the appropriate message.

    Returns:
        None
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if size == 0:
        return

    for _ in range(size):
        print("#" * size)
