#!/usr/bin/python3
"""Defines load_from_json_file function"""
import json


def load_from_json_file(filename):
    """
    Method that creates an Object from a “JSON file”:

    Args:
        filename: the name of the file to create a object from

    Returns:
        The Python object represented by the JSON in the file
    """
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
