#!/usr/bin/python3
"""Defines a base class for the Almost a Circle project"""


class Base:
    """The superclass of the Almost a circle project"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes the Base class

        Args:
            id: The identification for class initialization
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
