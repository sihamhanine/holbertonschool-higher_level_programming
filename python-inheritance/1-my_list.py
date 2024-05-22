#!/usr/bin/python3

"""Module my_list"""


class MyList(list):
    """
    MyList class inherits of list
    """

    def print_sorted(self):
        """
        Method that print sorted list
        """
        print(sorted(self))
