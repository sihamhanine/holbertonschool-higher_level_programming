#!/usr/bin/python3
from abc import ABC, abstractmethod


class Fish:
    """
    Defines a class Fish
    """
    def swim(self):
        """
        Method that print a message The fish is swimming
        """
        print("The fish is swimming")

    def habitat(self):
        """
        Method that print a message The fish lives in water
        """
        print("The fish lives in water")

class Bird:
    """
    Defines a class Bird
    """
    def fly(self):
        """
        Method that print a message The bird is flying
        """
        print("The bird is flying")

    def habitat(self):
        """
        Method that print a message The bird lives in the sky
        """
        print("The bird lives in the sky")
class FlyingFish(Fish, Bird):
    """
    Defines the class FlyingFish inherits from Fish and Bird
    """
    def fly(self):
        """
        Method that print a message The flying fish is soaring!
        """
        print("The flying fish is soaring!")

    def swim(self):
        """
        Method that print a message The flying fish is swimming!
        """
        print("The flying fish is swimming!")

    def habitat(self):
        """
        Method that print a message The flying fish lives both
        in water and the sky!
        """
        print("The flying fish lives both in water and the sky!")
