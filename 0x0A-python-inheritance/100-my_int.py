#!/usr/bin/python3

"""Defines a class MyInt"""


class MyInt(int):
    """Overrides the == and != signs"""

    def __eq__(self, value):
        """Returns the opposite of __eq__"""
        return super().__ne__(value)

    def __ne__(self, value):
        """Returns the opposite of __ne__"""
        return super().__eq__(value)
