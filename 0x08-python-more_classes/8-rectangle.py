#!/usr/bin/python3
"""This module defines a class Rectangle"""


class Rectangle:
    """This class defines a rectangle with with and height as instance
    attribues"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """This function initializes the rectangle using optional width and
        height
        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
                string += str(self.print_symbol)
            string += '\n'
        string += str(self.print_symbol) * self.width
        return (string)

    def __repr__(self):
        """Returns the string representation of the rectangle"""
        return ('Rectangle({:d}, {:d})'.format(self.width, self.height))

    def __del__(self):
        """Prints Bye rectangle... when a rectangle is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on area
        Args:
            rect_1 (Rectangle): rectangle 1
            rect_2 (Rectangle): rectangle 2
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        return rect_1
