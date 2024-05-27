#!/usr/bin/python3
"""Defines write_file function"""


def write_file(filename="", text=""):
    """
    Method that writes a string to a text file (UTF8)
    and returns the number of characters written

    Args:
        filename: the filename of the file to write in
        text: the text to write in file

    Returns:
        the number of characters written
    """
    with open(filename, "w", encoding='utf-8') as file:
        return file.write(text)
