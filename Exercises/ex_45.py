"""
Write a program for unit testing of a class.
Class Question that should be tested is defined in tested_code module.
There is a method store_answer() in the class that takes answer_text argument.

Rules for unit testing:
- prepare question needed for tests in setUp() method of the unit test class
- prepare list of answers also in setUp() method; you need four answers: "pool", "text", "float" and "real".
- use unit test to add answers and check if all the answers do exist
"""
import unittest
from tested_code import Question

class TestQuestion(unittest.TestCase):
    def setUp(self):
        self.my_question = Question("Select data types that is valid in Python")
        self.my_answer_texts = ["pool", "text", "float", "real"]

    """Test for Question class"""
    def test_store_answer(self):
        """Check if storing an answer is valid"""
        # Insert answers one by one
        for answer in self.my_answer_texts:
            self.my_question.store_answer(answer)

        # Check answers one by one if they are inside answers member of the class
        for answer in self.my_answer_texts:
            self.assertIn(answer, self.my_question.answers)

unittest.main()
