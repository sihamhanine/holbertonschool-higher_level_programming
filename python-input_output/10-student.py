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

    def to_json(self, attrs=None):
        """
        Method that retrieves a dictionary representation of a Student

        Args:
            attrs: the attributes of class initialite to None
        
        Returns:
            If attrs is a list of strings,
            only attributes name contained
            in this list must be retrieved.
            Otherwise, all attributes must be retrieved.
        """
        if isinstance(attrs, list):
            filtered_attributes = {}
            for key, value in self.__dict__.items():
                if key in attrs:
                    filtered_attributes[key] = value
            return filtered_attributes
        return self.__dict__
