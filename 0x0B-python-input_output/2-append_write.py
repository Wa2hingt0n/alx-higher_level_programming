#!/usr/bin/python3
"""Defines a function that appends text to a file and returns the number of
characters appended"""


def append_write(filename="", text=""):
    """Appends a string at the end of  a text file and returns the number of
       characters appended

    Args:
        filename: The file onto which text is to be appended
        text: String to be appended to filename
    """
    with open(filename, "a", encoding="utf-8") as a_file:
        return a_file.write(text)
