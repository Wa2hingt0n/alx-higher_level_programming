#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """Defines a square"""

    def __init__(self, size=0):
        """Initializes the square by size
        Args:
            size: Size of the square
        """

        self.size = size

    @property
    def size(self):
        """Property to retrieve the private instance of size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Property setting method for the size of the square
        Args:
            value: The set value of the square.
        Raises:
            TypeError: If the size is not an integer
            ValueError: If the size is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Computes the area of the square
        Returns:
            int: The area of the square
        """
        return (self.__size ** 2)

    def my_print(self):
        """Prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
        else:
            for i in range(0, self.__size):
                for j in range(0, self.__size):
                    print("#", end="")
                print()
