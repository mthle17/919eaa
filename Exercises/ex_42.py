"""
Write a program for unit testing of several functions.
Functions full_name, full_name_raw and full_name_reversed are defined in tested_code module.

Rules are as follows: 
- full_name('john', 'doe') should return 'John Doe'
- full_name_raw('john', 'doe') should return 'john doe'
- full_name_reversed('john', 'doe') should return 'Doe, John'

If unit tests fail, instead of raising an error print message "Tests failed".
"""
import unittest
from tested_code import full_name, full_name_raw, full_name_reversed

class FullNameUnitTests(unittest.TestCase):
    """Test for full_name function"""
    def test_full_name(self):
        res = full_name('john', 'doe')
        self.assertEqual(res, 'John Doe')

    """Test for full_name_raw function"""
    def test_full_name_raw(self):
        res = full_name_raw('john', 'doe')
        self.assertEqual(res, 'john doe')

    """Test for full_name_reversed function"""
    def test_full_name_reversed(self):
        res = full_name_reversed('john', 'doe')
        self.assertEqual(res, 'Doe, John')

try:
    unittest.main()
except:
    print("Tests failed")
