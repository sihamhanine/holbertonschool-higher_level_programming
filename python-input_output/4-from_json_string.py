#!/usr/bin/python3
"""Defines from_json_string function"""
import json


def from_json_string(my_str):
    """
    Method that returns an object (Python data structure)
    represented by a JSON string

    Args:
        my_str: the json string

    Returns:
        an object (Python data structure)
    """
    return json.loads(my_str)
