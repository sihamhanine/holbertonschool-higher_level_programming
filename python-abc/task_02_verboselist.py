#!/usr/bin/python3
from abc import ABC, abstractmethod


class VerboseList(list):
    """
    Defines the class VerboseList inherits from list
    """
    def append(self, item):
        """
        Method that append a element in the end list

        Args:
            item: the element to append
        """
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, items):
        """
        Method that append the elements at the end of list
        
        Args:
            items: ensemble the elements to append
        """
        super().extend(items)
        print("Extended the list with [{}] items.".format(len(items)))

    def remove(self, item):
        """
        Method that remove an element in the list

        Args:
            item: the element to remove
        """
        print("Removed [{}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """
        Method that remove an element at the index

        Args:
            index: the index to remove their element

        Returns:
            the element removed
        """
        try:
            item_removed = super().pop(index)
            print("Popped [{}] from the list.".format(item_removed))
            return item_removed
        except IndexError:
            print("Index out of range. Cannot pop from an empty list.")
            return None
