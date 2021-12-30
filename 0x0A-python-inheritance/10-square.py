#!/usr/bin/python3
"""Defines a class Square"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Describes a square and inherits from class Rectangle"""
    def __init__(self, size):
        """Initializes the square by its size

        Args:
            size (int): Size of the square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Computes the area of the square"""
        return self.__size ** 2
