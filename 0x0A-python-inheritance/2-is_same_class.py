#!/usr/bin/python3

"""Defines a function is_same_object"""


def is_same_class(obj, a_class):
    """Checks if an object is exactly an instance of the specified class

    Args:
        obj: The instance to be checked
        a_class: The class to be compared to

    Returns:
        True: If obj is exactly an instance of a_class
        False: Otherwise
    """
    if type(obj) == a_class:
        return True
    return False
