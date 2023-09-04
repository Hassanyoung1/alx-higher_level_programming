#!/usr/bin/python3

def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a given divisor.

    Args:
        matrix (list of lists): The input matrix, where each row is a list of integers or floats.
        div (int or float): The divisor used for division.

    Returns:
        list of lists: A new matrix with elements divided by the divisor, rounded to 2 decimal places.

    Raises:
        TypeError: If the input matrix is not a list of lists containing integers or floats,
                   if the rows of the matrix have different sizes, or if the divisor is not a number.
        ZeroDivisionError: If the divisor is equal to 0.
    """
    if not all(isinstance(row, list) and all(isinstance(num, (int, float)) for num in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_len = len(matrix[0])
    if not all(len(row) == row_len for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = [round(num / div, 2) for num in row]
        new_matrix.append(new_row)

    return new_matrix
