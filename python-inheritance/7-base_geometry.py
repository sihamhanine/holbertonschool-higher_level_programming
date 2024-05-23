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
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
