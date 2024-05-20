#!/usr/bin/python3

"""Module for say_my_name method"""


def say_my_name(first_name, last_name=""):
    """method say_my_name that print my name is
    <first name> <last name>

    Args:
        first_name: the first name in string
        last_name: the last name in string

    Raises:
        TypeError: first_name must be a string
        TypeError: last_name must be a string
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))


if __name__ == "__main__":
    import doctest
    doctest.filetest("tests/3-say_my_name.txt")
