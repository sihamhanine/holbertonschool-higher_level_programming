#!/usr/bin/python3
""" Defines class_to_json function"""


def class_to_json(obj):
    """
    Method that returns the dictionary description with
    simple data structure for JSON serialization of an object

    Args:
        obj: the object to return hir dictionnary

    Returns:
        the dictionnary description of an object
    """
    return obj.__dict__
