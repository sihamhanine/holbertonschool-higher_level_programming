#!/usr/bin/python3
"""Defines the function of serialization and deserialization"""
import json


def serialize_and_save_to_file(data, filename):
    """
    Method that to serialize and save data to the specified file

    Args:
        data: A Python Dictionary with data
        filename: The filename of the output JSON file.
                If the output file already exists it should be replaced.
    """
    with open(filename, "w", encoding='utf-8') as file:
        json.dump(data, file)

def load_and_deserialize(filename):
    """
    Method that returns a Python Dictionary with the deseialized
    JSON data from the file

    Args:
        filename: The filename of the input JSON file
    Returns:
        python dictionnary deserialisé
    """
    with open(filename, "r", encoding='utf-8') as file:
        return json.load(file)
