#!/usr/bin/python3
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Defines a class Shape
    """
    @abstractmethod
    def area(self):
        """
        Empty abstract method area
        """
        pass
    @abstractmethod
    def perimeter(self):
        """
        A empty abstract method perimeter
        """
        pass

class Circle(Shape):
    """
    Defines a class Circle inherits from Shape
    """
    def __init__(self, radius):
        """
        The constructor of the class Circle

        Args:
            radius: the radius of the class Circle
        """
        self.radius = radius

    def area(self):
        """
        Method that return the area of the class Circle

        Returns:
            area of circle
        """
        return abs(math.pi * (self.radius ** 2))

    def perimeter(self):
        """
        Method that return the perimeter of the class Circle

        Returns:
            perimeter of circle
        """
        return abs(2 * math.pi * self.radius)

class Rectangle(Shape):
    """
    Defines the class Rectangle inherits from Shape
    """
    def __init__(self, width, height):
        """
        The constructor to initialize attributes

        Args:
            width: the width of the class Rectangle
            height: the height of the class Rectangle
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Method that return area of rectangle

        Returns:
            area of the Rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """
        Method that return the perimeter of rectangle

        Returns:
            perimeter of the class Rectangle
        """
        return 2 * (self.width + self.height)

def shape_info(shape):
    """
    Method that print the area and perimeter of the shape

    Args:
        shape: the object to print their info
    """
    try:
        shape_area = shape.area()
        shape_perimeter = shape.perimeter()
        print("Area: {}".format(shape_area))
        print("Perimeter: {}".format(shape_perimeter))
    except AttributeError as e:
        print(f"Error: {e}")
