#!/usr/bin/python3
"""Defines a function class_to_json"""


def class_to_json(obj):
    """Returns dictionary description with simple data structure for JSON
    serialization for an object"""
    return obj.__dict__
