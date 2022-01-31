"""
Write a program for unit testing of the function.
Function full_name() is defined in tested_code module.
Function takes first and last name as parameters, and returns capitalized full name.
Example: full_name('john', 'doe') should return 'John Doe'
"""
import unittest
from tested_code import *

class FullNameUnitTests(unittest.TestCase):
    def test_full_name(self):
        res = full_name('john', 'doe')
        self.assertEqual(res, 'John Doe')

unittest.main()
