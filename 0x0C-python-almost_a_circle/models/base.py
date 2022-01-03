#!/usr/bin/python3
"""Defines a base class for the Almost a Circle project"""


import json


class Base:
    """The superclass of the Almost a circle project"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes the Base class

        Args:
            id: The identification for class initialization
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns the JSON string representation of a list of dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Writes the JSON string representation of list_objs to a file

        Args:
            list_objs (list): A list of instances that inherit from Base
        """
        with open(cls.__name__ + '.json', mode='w') as f:
            if list_objs is None:
                f.write("[]")
            else:
                json_list = []
                for obj in list_objs:
                    json_list.append(obj.to_dictionary())
                if len(json_list) > 0:
                    f.write(Base.to_json_string(json_list))

    def from_json_string(json_string):
        """ Returns the list of the JSON string representation json_string

        Args:
            json_string: The string to be deserialized
        """
        if json_string is None or json_string == "[]":
            return []
        else:
            return json.loads(json_string)
