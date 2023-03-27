import unittest
from string_functions import *

class TestToUpper(unittest.TestCase):
    # write your code here
    def test_upper(self):
        self.assertEqual(to_upper("hello"), "HELLO")
        self.assertEqual(to_upper("WORLD"), "WORLD")
        self.assertEqual(to_upper("123"), "123")
        self.assertEqual(to_upper(""), "")
        self.assertEqual(to_upper("hElLo"), "HELLO")

class TestToLower(unittest.TestCase):
    def test_lower(self):
        self.assertEqual(to_lower("HELLO"), "hello")
        self.assertEqual(to_lower("world"), "world")
        self.assertEqual(to_lower("123"), "123")
        self.assertEqual(to_lower(""), "")
        self.assertEqual(to_lower("HeLlO"), "hello")
    # Write you code here
  

class TestCapitalize(unittest.TestCase):
    # Write your code here
    def test_capitalize(self):
        self.assertEqual(capitalize("hello"), "Hello")
        self.assertEqual(capitalize("WORLD"), "World")
        self.assertEqual(capitalize("123"), "123")
        self.assertEqual(capitalize(""), "")
        self.assertEqual(capitalize("hElLo"), "Hello")

if __name__ == '__main__':
    unittest.main()
