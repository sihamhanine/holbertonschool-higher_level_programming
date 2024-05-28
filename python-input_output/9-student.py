#!/usr/bin/python3
"""Defines module student"""


class Student:
    """Defines a class"""

    def __init__(self, first_name, last_name, age):
        """
        Method that instantiate the attribute of a class

        Args:
            first_name: the first name
            last_name: the last name
            age: the age of student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Method that retrieves a dictionary representation of a Student
        """
        return self.__dict__
