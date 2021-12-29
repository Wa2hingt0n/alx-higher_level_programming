#!/usr/bin/python3

"""Defines a function inherits_from"""


def inherits_from(obj, a_class):
    """Checks whether an object is an instance of a class that inherited from
    the specified class

    Args:
        obj: The object to be checked
        a_class: The superclass

    Returns:
        True: If the object is an instance a class that inherited from the
        specified class
        False: Otherwise
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
