#!/usr/bin/python3
"""
This module defines a Square class with a private instance attribute `size`.
"""

class Square:
    """
    Represents a square.

    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size):
        """
        Initializes the square with the given size.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
