#!/usr/bin/python3

"""Module for matrix_divided method"""


def matrix_divided(matrix, div):
    """Method matrix_divided that divides all elements of a matrix by div.

    Args:
        matrix: List of lists containing int or float
        div: The number to divide by int or float

    Raises:
        TypeError: matrix must be a matrix (list of lists) of integers/floats 
        TypeError: Each row of the matrix must have the same size
        TypeError: div must be a number
        ZeroDivisionError: division by zero

    Returns:
        A new matrix with a divided elements
    """
    if not type(div) in (int, float):
        raise TypeError("div must be a number")
    if not type(matrix) is list or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for row in matrix:
        if not type(row) is list or len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    for row in matrix:
        row_divided = []
        for elem in row:
            divided_elem = round(elem / div, 2)
            row_divided.append(divided_elem)
        new_matrix.append(row_divided)
    return new_matrix


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
