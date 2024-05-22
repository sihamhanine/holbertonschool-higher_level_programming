#!/usr/bin/python3

"""Module inherits_from"""


def inherits_from(obj, a_class):
    """
    Method that returns True if the object is an instance of a class that
    inherited (directly or indirectly) from the specified class ;
    otherwise False.

    Args:
        obj: the object to verify
        a_class: a class specified

    Returns:
        True if the object is instance of class that inherited
        False otherwise
    """
    if isinstance(obj, a_class) and
       issubclass(a_class, obj.__class__) is False:
        return True
    return False
