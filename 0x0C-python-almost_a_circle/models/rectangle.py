#!/usr/bin/python3
"""The rectangle module"""


from models.base import Base


class Rectangle(Base):
    """Defines the class Rectangle with the superclass Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes the instance attributes of the Rectangle class

        Args:
            width: The width of the rectangle
            height: The height of the rectangle
            x: Horizontal coordinate of the rectangle
            y: Verticle rectangle coordinate
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Getter for the width private attribute"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the width private attribute

        Args:
            value: The value of the width
        """
        self.__width = value

    @property
    def height(self):
        """Getter for the height private attribute"""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the height private attribute

        Args:
            value: The value of the height
        """
        self.__height = value

    @property
    def x(self):
        """Getter for the x private attribute"""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for the x private attribute

        Args:
            value: The value of the x coordinate
        """
        self.__x = value

    @property
    def y(self):
        """Getter for the y private attribute"""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for the y private attribute

        Args:
            value: The value of the y coordinate of the rectangle
        """
        self.__y = value
