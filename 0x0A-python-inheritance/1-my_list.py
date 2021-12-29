#!/usr/bin/python3

"""Defines a class MyList that inherits from list"""


class MyList(list):
    """Defines a subclass MyList of the baseclass list"""
    def print_sorted(self):
        """Prints a list sorted in ascending order"""
        new = self[:]
        new.sort()
        print(new)
