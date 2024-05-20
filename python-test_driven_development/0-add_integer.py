#!/usr/bin/python3
"""Module add_integer"""

def add_integer(a, b=98):
    """ Method add_integer une fonction that add 2 integers 
    when they must be integers or float, and return the result

    Args:
        a: int or float the first number
        b: int or float the second number default 98

    Raises:
        TypeError: a et b not an int or float

    Returns:
        the sum of two integers
    """
    if type(a) not in (int, float):
        raise TypeError('a must be an integer')
    if type(b) not in (int, float):
        raise TypeError('b must be an integer')

    return int(a) + int(b)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")