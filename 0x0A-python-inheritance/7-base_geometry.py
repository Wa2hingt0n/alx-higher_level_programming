#!/usr/bin/python3

"""Defines a class BaseGeometry"""


class BaseGeometry:
    """Defines a class BaseGeometry"""
    def area(self):
        """Raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value

        Args:
            name (str): The name that is always a string
            value (int): The value to be validated
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
