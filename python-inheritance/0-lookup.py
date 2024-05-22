#!/usr/bin/python3

"""Module lookup"""


def lookup(obj):
    """Method that returns the list of available attributes
    and methods of an object

    Args:
        obj: the obj to return there attributes and methods

    Returns:
        The object with methods and attributes
    """
    return dir(obj)
    