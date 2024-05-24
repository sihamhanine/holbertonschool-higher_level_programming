#!/usr/bin/python3
from abc import ABC, abstractmethod


class SwimMixin:
    """
    Defines a class SwimMixin
    """
    def swim(self):
        """
        Method that print a message The creature swims!
        """
        print("The creature swims!")

class FlyMixin:
    """
    Defines a class FlyMixin
    """
    def fly(self):
        """
        Method that print a message The creature flies!
        """
        print("The creature flies!")

class Dragon(SwimMixin, FlyMixin):
    """
    Defines a class Dragon
    """
    def roar(self):
        """
        Method that print a message The dragon roars!
        """
        print("The dragon roars!")
