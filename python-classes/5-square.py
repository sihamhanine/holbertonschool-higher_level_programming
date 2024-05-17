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
        self.__size = size

    @property
    def size(self):
        """
        Getter method for retrieving the size attribute.
        
        Returns:
        -------
        int
            The size of the square's sides.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for setting the size attribute.
        
        Parameters:
        ----------
        value : int
            The size to set for the square's sides.
        
        Raises:
        ------
        TypeError:
            If value is not an integer.
        ValueError:
            If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Returns the current square area.
        
        Returns:
        -------
        int
            The area of the square.
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Prints the square with the character #.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)