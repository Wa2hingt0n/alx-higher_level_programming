#!/usr/bin/python3

"""Defines a class Square"""


class Square:
    """Defines a square"""

    def __init__(self, size=0):
        """Initializes the class Square

        Args:
            size (int): The size of the square

        Raises:
            TypeError: If `size` is not an integer
            ValueError: If `size` iis less than 0

        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
