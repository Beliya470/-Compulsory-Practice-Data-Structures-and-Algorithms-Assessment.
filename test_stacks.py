import unittest
from stacks import is_balanced

class TestStackFunctions(unittest.TestCase):

    def test_is_balanced(self):
        self.assertTrue(is_balanced("([]{})"))
        self.assertFalse(is_balanced("([)]"))
        # Add more test cases if needed

if __name__ == '__main__':
    unittest.main()
