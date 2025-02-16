import unittest
from str_split import str_split

class TestGetMaxIncrease(unittest.TestCase):
    def test_zero_space(self):
        self.assertEqual(str_split("helloworld"), "helloworld")

    def test_one_space(self):
        self.assertEqual(str_split("hello my world here"), "hello my world here")

    def test_multiple_spaces(self):
        self.assertEqual(str_split("hello  my   world     here"), "hello my world here")

    def test_space_before_after_str(self):
        self.assertEqual(str_split("      hello my world here        "), " hello my world here ")

if __name__ == '__main__':
    unittest.main()