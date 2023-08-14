#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):

    if matrix:
        for element in matrix:
            for num in element:
                print("{:d}".format(num), end="")
                if element.index(num) != len(element) - 1:
                    print(" ", end="")
            print()


