#!/usr/bin/python3
from abc import ABC, abstractmethod


class CountedIterator:
    """
    Defines the class CountedIterator
    """
    def __init__(self, iterable):
        """
        The constructor of the class

        Args:
            iterable: the iterator object 
        """
        self.iterator = iter(iterable)
        self.counter = 0

    def get_count(self):
        """
        Method that return the current value of the counter.

        Returns:
            current value of counter
        """
        return self.counter

    def __next__(self):
        """
        Method that increment the counter and fetch
        the next item from the iterator object

        Returns:
            the value of counter incremented
        """
        try:
            item = next(self.iterator)
            self.counter += 1
            return item
        except StopIteration:
            raise StopIteration("End of iteration")
