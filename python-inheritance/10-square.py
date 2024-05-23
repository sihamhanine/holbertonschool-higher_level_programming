#!/usr/bin/python3

"""Module for Rectangle class."""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    Class Square inherits from Rectangle
    """
    def __init__(self, size):
        """
        Constructor inherits

        Args:
            size: the size og rectangle
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """
        Method to return area from square
        """
        return self.__size ** 2
