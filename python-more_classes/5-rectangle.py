#!/usr/bin/python3

"""Module for 1-rectangle method"""


class Rectangle:
    """
    A class that defines a rectangle by its width.
    Attributes:
    ----------
    __width : int
        The width of the rectangle's sides.
    __height : int
        The height of the rectangle's sides
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle instance with the specified width.
        Parameters:
        ----------
        width : int
            The width of the rectangle's sides.
        height : int
            The height of the rectangle's sides.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Returns the width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Verify the parameters and set the width of rectangle

        Args:
            value: int the width of the rectangle

        Raises:
            TypeError: width must be an integer
            ValueError: width must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Returns the height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Verify the parameters and set the height of rectangle

        Args:
            value: int the height of the rectangle

        Raises:
            TypeError: height must be an integer
            ValueError: height must be >= 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Returns the rectangle area
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculate the perimeter of rectangle
        """
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __str__(self):
        """
        Print the rectangle with the character #
        if width and height is 0 return a empty string
        """
        if self.width == 0 or self.height == 0:
            return ""
        rectangle_str = ""
        for i in range(self.height):
            rectangle_str += self.width * "#"
            if i < self.height - 1:
                rectangle_str += "\n"
        return rectangle_str

    def __repr__(self):
        """
        Returns a string representation of the rectangle for debugging

        The string is formatted as: Rectangle(width, height)
        """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """
        Print a message when an instance of rectangle is deleted
        """
        print("Bye rectangle...")
