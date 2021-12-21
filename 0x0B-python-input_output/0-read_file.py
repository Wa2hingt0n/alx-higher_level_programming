#!/usr/bin/python3
"""Defines a function to read files and print result to stdout"""


def read_file(filename=""):
    """Reads a text file and prints it to stdout"""
    with open(filename, mode="r", encoding="utf-8") as a_file:
        print(a_file.read(), end="")
