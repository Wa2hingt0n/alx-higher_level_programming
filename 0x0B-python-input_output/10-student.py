#!/usr/bin/python3
"""Defines a class Student"""


class Student:
    """Defines a student"""
    def __init__(self, first_name, last_name, age):
        """Initializes the student

        Args:
            first_name (int): Fisrt name of Student
            last_name (int): Last name of Student
            age (int): Student's age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance"""
        obj_dict = self.__dict__
        if not attrs:
            return obj_dict
        else:
            filter_dict = {}
            for att in attrs:
                if hasattr(self, att):
                    filter_dict[att] = obj_dict[att]
            return filter_dict
