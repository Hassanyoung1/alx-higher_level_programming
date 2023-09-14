#!/usr/bin/python3

""" Declare Function prototype  """


def pascal_triangle(n):
    """
    Generate Pascal's triangle up to the nth row.

    Args:
        n (int): The number of rows in Pascal's triangle to generate.

    Returns:
        list: A list of lists of integers representing Pascal's triangle.
              An empty list is returned if n is less than or equal to 0.
    """
    if n <= 0:
        return []

    # Initialize the Pascal's triangle with the first row
    triangle = [[1]]

    for i in range(1, n):
        # Create the next row
        row = [1]
        for j in range(1, i):
            # Calculate the values based on the previous row
            value = triangle[i - 1][j - 1] + triangle[i - 1][j]
            row.append(value)
        row.append(1)
        triangle.append(row)

    return triangle
