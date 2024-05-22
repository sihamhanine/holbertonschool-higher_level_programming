#!/usr/bin/python3

"""Module is_kin_of_class"""


def is_kind_of_class(obj, a_class):
    """
    Method that returns True if the object is an instance of, or if the object
    is an instance of a class that inherited from, the specified class ;
    otherwise False.

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
