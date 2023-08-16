#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Create a new matrix to store the squared values
    result_matrix = []

    # Iterate through the rows of the input matrix
    for row in matrix:
        # Create a new row for the result matrix
        result_row = []

        # Iterate through the elements in the current row
        for value in row:
            # Compute the square of the value and append to the result row
            result_row.append(value ** 2)

        # Append the result row to the result matrix
        result_matrix.append(result_row)

    return result_matrix
