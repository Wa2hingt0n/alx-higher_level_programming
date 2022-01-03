#!/usr/bin/python3

""" Defines a class square """

from models.rectangle import Rectangle


class Square(Rectangle):
    """ Defines a class square that inherits from class Rectangle """
    def __init__(self, size, x=0, y=0, id=None):
        """ Initializes the square

        Args:
            size (int): The size of the square
            x (int): The horizontal offset of the square
            y (int): Vertical offset of the square
            id (int): Id of the square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Public getter for the size attribute """
        return self.width

    @size.setter
    def size(self, value):
        """ Public setter for the size attribute

        Args:
            value (int): The size of the square
        """
        self.width = value
        self.height = value

    def __str__(self):
        """ Overloads the __str__ method """
        string = "[{}] ({:d}) {:d}/{:d} - {:d}".format(
            type(self).__name__, self.id, self.x, self.y, self.width)
        return string

    def update(self, *args, **kwargs):
        """ Updates the class Square by assigning attributes

        Args:
            args: Variable list of non key-worded arguments
                - 1st argument: id
                - 2nd argument: size
                - 3rd argument: x
                - 4th argument: y
        """
        if len(args) > 0:
            i = 1
            for arg in args:
                if i == 1:
                    self.id = arg
                elif i == 2:
                    self.width = arg
                elif i == 3:
                    self.x = arg
                elif i == 4:
                    self.y = arg
                i += 1
        elif len(kwargs) > 0:
            for k, v in kwargs.items():
                if k == "id":
                    self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """ Returns the dictionary representation of a Square """
        return {"id": self.id, "size": self.width, "x": self.x, "y": self.y}
