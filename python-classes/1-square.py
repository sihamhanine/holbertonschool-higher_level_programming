#!/usr/bin/python3

"""Square class"""


class Square:
    """
    A class that defines a square by its size.
    
    Attributes:
    ----------
    __size : int
        The size of the square's sides.
    """

    def __init__(self, size):
        """
        Initializes a new Square instance with the specified size.
        
        Parameters:
        ----------
        size : int
            The size of the square's sides.
        """
        self.__size = size
        