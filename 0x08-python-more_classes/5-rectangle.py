#!/usr/bin/python3
"""This module defines a class Rectangle"""


class Rectangle:
    """This class defines a rectangle with with and height as instance
    attribues"""
    def __init__(self, width=0, height=0):
        """This function initializes the rectangle using optional width and
        height
        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle
        Args:
            value (int): The value to set as the width of the rectangle
        Raises:
            TypeError: If width is not an integer
            ValueError: If width is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width mus be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle
        Args:
            value (int): Height of the rectangle
        Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle"""
        return (self.width * self.height)

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return ((self.width * 2) + (self.height * 2))

    def __str__(self):
        """String representation of a rectangle using the # character.
        Returns:
            string rep of rectangle
        """
        string = ''
        if self.width == 0 or self.height == 0:
            return string
        for i in range(self.height - 1):
            for j in range(self.width):
                string += '#'
            string += '\n'
        string += '#' * self.width
        return (string)

    def __repr__(self):
        """Returns the string representation of the rectangle"""
        return ('Rectangle({:d}, {:d})'.format(self.width, self.height))

    def __del__(self):
        """Prints Bye rectangle... when a rectangle is deleted"""
        print("Bye rectangle...")
