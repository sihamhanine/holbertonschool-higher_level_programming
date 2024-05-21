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
