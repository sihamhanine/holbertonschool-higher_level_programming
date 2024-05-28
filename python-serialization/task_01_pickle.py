#!/usr/bin/python3
"""Defines module task_01_pickle"""
import pickle


class CustomObject:
    """
    Defines a class CustomObject
    """
    def __init__(self, name, age, is_student):
        """
        Constructor of the class CustomObject

        Args:
            name: the name of person in string
            age: the age of person en integer
            is_student: true or false
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Method that print out the object’s attributes
        """
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """
        Method that serialize the current instance of the object
        and save it to the provided filename.

        Args:
            filename: the file to provid in an object serialized
        """
        with open(filename, "wb") as file:
            pickle.dump(self, file)

    @classmethod
    def deserialize(cls, filename):
        """
        Method that load and return an instance of
        the CustomObject from the provided filename

        Args:
            filename: the file to provid in an object deserialized
            cls: an instance of object
        Returns:
            an instance the CustomObject
        """
        with open(filename, "rb") as file:
            return pickle.load(file)
