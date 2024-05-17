#!/usr/bin/python3
"""Square class"""
class Square:
    """
    A class that defines a square by its size and position.
    
    Attributes:
    ----------
    __size : int
        The size of the square's sides.
    __position : tuple
        The position of the square's top-left corner.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new Square instance with the specified size and position.
        
        Parameters:
        ----------
        size : int, optional
            The size of the square's sides (default is 0).
        position : tuple, optional
            The position of the square's top-left corner (default is (0, 0)).
        
        Raises:
        ------
        TypeError:
            If size is not an integer or position is not a tuple of 2 positive integers.
        ValueError:
            If size is less than 0 or position contains non-positive integers.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        Getter method for retrieving the position attribute.
        
        Returns:
        -------
        tuple
            The position of the square's top-left corner.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter method for setting the position attribute.
        
        Parameters:
        ----------
        value : tuple
            The position to set for the square's top-left corner.
        
        Raises:
        ------
        TypeError:
            If value is not a tuple of 2 positive integers.
        ValueError:
            If value contains non-positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2 or not all(isinstance(x, int) for x in value) or any(x < 0 for x in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
        Prints the square with the character #, respecting the position attribute.
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)