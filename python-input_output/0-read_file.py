#!/usr/bin/python3
"""Defines read_file function"""


def read_file(filename=""):
    """
    Method that read a texts file and print
    it to stdout

    Args:
        filename: the name of file to read
    """
    with open(filename, "r", encoding='utf-8') as file:
        content_file = file.read()
        print(content_file, end="")
