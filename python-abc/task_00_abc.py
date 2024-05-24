#!/usr/bin/python3
from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Defines the class
    """
    @abstractmethod
    def sound(self):
        """
        A empty abstract method
        """
        pass

class Dog(Animal):
    """
    Defines a Dog class inherits from Animal
    """
    def sound(self):
        """
        Method that return the string Bark
        """
        return "Bark"

class Cat(Animal):
    """
    Defines a Cat class inherits from Animal
    """
    def sound(self):
        """
        Method that return the string Meow
        """
        return "Meow"
