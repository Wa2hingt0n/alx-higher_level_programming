#!/usr/bin/python3
"""Defines a function append_after"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text to a file after each line containing a specific
    string

    Args:
        filename: The name of the file to be searched and written onto
        search_string: String to be searched
        new_string: String to append to filename
    """
    text = ""
    with open(filename) as a_file:
        for line in a_file:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as w:
        w.write(text)
