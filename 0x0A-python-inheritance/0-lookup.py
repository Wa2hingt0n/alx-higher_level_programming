#!/usr/bin/python3

"""Defines a method lookup"""


def lookup(obj):
    """Returns a list of available attributes and methods of an object"""
    return dir(obj)
