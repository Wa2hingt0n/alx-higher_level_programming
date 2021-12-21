#!/usr/bin/python3
"""Defines a function that writes a string to a text file"""


def write_file(filename="", text=""):
    """Writes a string to a text file and returns the number of characters
    written

    The file should be created if it doesn't exist and should overwrite content

    Args:
        filename: The name of the file to write to
        text: String to be written onto filename
    """
    with open(filename, 'w', encoding="utf-8") as a_file:
        return a_file.write(text)
