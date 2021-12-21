#!/usr/bin/python3
"""Defines a function that returns the JSON reresentation of an object(string)
"""
import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object (string)

    Args:
        my_obj: The object to be serialized
    """
    return json.dumps(my_obj)
