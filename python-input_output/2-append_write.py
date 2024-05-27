#!/usr/bin/python3
"""Defines append_write function"""


def append_write(filename="", text=""):
    """
    Method that appends a string at the end of a text file (UTF8)
    and returns the number of characters added:

    Args:
        filename: the filename the file to append a string in
        text: the text to append in file

    Returns:
        the number of characters added
    """
    with open(filename, "a", encoding='utf-8') as file:
        return file.write(text)
