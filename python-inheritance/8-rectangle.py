#!/usr/bin/python3
BaseGeometry = __import__("7-base_geometry").BaseGeometry
"""Module Rectangle"""


class Rectangle(BaseGeometry):
    """
    Class Rectangle inherits from BaseGeometry
    """
    def __init__(self, width, height):
        """
        Constructor inherits
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
