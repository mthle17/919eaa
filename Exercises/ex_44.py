"""
Write a program for unit testing of a class.
Class Question that should be tested is defined in tested_code module.
There is a method store_answer() in the class that takes answer_text argument.

Rules for unit testing:
- create instance of Question class
- using method store_answer() add four answers: "pool", "text", "float" and "real".
- use unit test to check if all the answers do exist ("pool", "text", "float" and "real")
"""
import unittest
from tested_code import Question

class TestQuestion(unittest.TestCase):
    """Test for Question class"""
    def test_store_answer(self):
        """Check if storing an answer is valid"""
        my_question = Question("Select data types that is valid in Python")
        my_question.store_answer("pool")
        my_question.store_answer("text")
        my_question.store_answer("float")
        my_question.store_answer("real")

        for answer in ["pool", "text", "float", "real"]:
            self.assertIn(answer, my_question.answers)

unittest.main()
