#!/usr/bin/python3
"""Defines a class TestBase for testing the base module"""


from models.base import Base
import unittest


class TestBase(unittest.TestCase):
    """Test class for the methods of the base module"""
    def test_id_initialization(self):
        """Tests the instansiation of the class Base"""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(12)
        b5 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        self.assertEqual(b4.id, 12)
        self.assertEqual(b5.id, 4)


if __name__ == '__main__':
    unittest.main()
