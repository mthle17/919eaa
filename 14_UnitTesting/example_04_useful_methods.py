import unittest

class TestSum(unittest.TestCase):
    def setUp(self):
        self.data = [1, 2, 3]

    def test_list_init(self):
        result = sum(self.data)
        self.assertEqual(result, 6)

    def tearDown(self):
        print("Finished testing")

if __name__ == "__main__":
    unittest.main() # run unit tests
