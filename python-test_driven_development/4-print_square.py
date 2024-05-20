#!/usr/bin/python3

"""Module for 4-print_square method"""


def print_square(size):
    """Method that prints a square with the character #.

    Args:
        size: the size lenght of the square

    Raises:
        TypeError: size must be an integer
        ValueError: if size < 0 size must be >= 0
        TypeError: if size is float and < 0
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
