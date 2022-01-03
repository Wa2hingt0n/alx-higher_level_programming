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
            x: Horizontal offset of the rectangle
            y: Vertical offset of the rectangle
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
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
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
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
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
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
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
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Returns the area of the rectangle"""
        return self.width * self.height

    def display(self):
        """Prints the rectangle instance with the # character to stdout"""
        for vert_off in range(0, self.y):
            print()
        for i in range(0, self.height):
            for hor_off in range(0, self.x):
                print(" ", end="")
            for j in range(0, self.width):
                print("#", end="")
            print()

    def __str__(self):
        """Overrides the __str__ method to print some custom text"""
        string = "[{}] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            type(self).__name__, self.id, self.x, self.y, self.width,
            self.height)
        return string

    def update(self, *args, **kwargs):
        """Updates the class Rectangle by assigning an argument to each
        attribute

        Args:
            args: Variable number of non key-worded arguments
            kwargs: Variable number of key-worded arguments
        """
        if len(args) > 0:
            i = 1
            for arg in args:
                if i == 1:
                    self.id = arg
                elif i == 2:
                    self.width = arg
                elif i == 3:
                    self.height = arg
                elif i == 4:
                    self.x = arg
                elif i == 5:
                    self.y = arg
                i += 1
        elif len(kwargs) > 0:
            for k, v in kwargs.items():
                if k == "id":
                    self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """ Returns the dictionary representation of Rectangle """
        return {"id": self.id, "width": self.width, "height": self.height,
                "x": self.x, "y": self.y}
