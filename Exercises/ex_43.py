"""
Write a program for unit testing of a class.
Class Question that should be tested is defined in tested_code module.
There is a method store_answer() in the class that takes answer_text argument.

Rules for unit testing:
- create instance of Question class
- using method store_answer() add an answer: "float"
- use unit test to check that there is a value "float" in answers
"""
import unittest
from tested_code import Question

class TestQuestion(unittest.TestCase):
    """Test for Question class"""
    def test_store_answer(self):
        """Check if storing an answer is valid"""
        my_question = Question("Select data types that is valid in Python")
        my_question.store_answer("float")

        self.assertIn("float", my_question.answers)
        
unittest.main()
