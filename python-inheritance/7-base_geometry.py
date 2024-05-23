#!/usr/bin/python3

"""Module base_geometry"""


class BaseGeometry:
    """
    Class BaseGeometry
    """
    def area(self):
        """
        Method to raise a msg erreur
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Method to validate integer

        Args:
            name (str): The name of the parameter.
            value (int): The value to validate.
        
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
