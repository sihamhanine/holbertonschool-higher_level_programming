#!/usr/bin/python3
"""Defines save_to_json_file function"""
import json


def save_to_json_file(my_obj, filename):
    """
    Method that writes an Object to a text file,
    using a JSON representation

    Args:
        my_obj: the object to be serialized to JSON and written to the file.
        filename: the name of the file to write the JSON representation to.
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
