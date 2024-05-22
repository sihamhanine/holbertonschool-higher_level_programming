#!/usr/bin/python3

"""Module is_same_class"""


def is_same_class(obj, a_class):
    """
    Method that returns True if the object is exactly
    an instance of the specified class ; otherwise False.

    Args:
        obj: the object to verify
        a_class: a class specified

    Returns:
        True if the object is instance of class
        False otherwise
    """
    if not isinstance(obj, a_class):
        return False
    return True
