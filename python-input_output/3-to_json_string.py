#!/usr/bin/python3
"""Defines ato_json_string function"""
import json


def to_json_string(my_obj):
    """
    Method that returns the JSON representation
    of an object (string):

    Args:
        my_obj: the json object

    Returns:
        the JSON represent of an object
    """
    return json.dumps(my_obj)
