#!/usr/bin/python3
"""The test modul for the recatngle module"""


import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test class for the the methods of the rectangle module"""
    def test_rectangle_initialization(self):
        """Tests the initialization of the class"""
        r1 = Rectangle()
        r2 = Rectangle(2)
        r3 = Rectangle(2, 5)
        r4 = Rectangle(2, 5, 3)
        r5 = Rectangle(2, 5, 3, 7)
        r6 = Rectangle(2, 5, 3, 7, 5)
        self.assertEqual(print(r1.id), )
