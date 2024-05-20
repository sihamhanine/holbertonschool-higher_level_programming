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

    def __init__(self, size=0):
        """
        Initializes a new Square instance with the specified size.
        
        Parameters:
        ----------
        size : int, optional
            The size of the square's sides (default is 0).
        
        Raises:
        ------
        TypeError:
            If size is not an integer.
        ValueError:
            If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        