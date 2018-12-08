import unittest
from fizzbuzz import *


class FizzBuzz(unittest.TestCase):

    def test_000(self):
        self.assertEqual(fizzbuzz(0), "FizzBuzz")

    def test_001(self):
        self.assertEqual(fizzbuzz(15), "FizzBuzz")

    def test_002(self):

        for i in range(3,15,3):
            self.assertEqual(fizzbuzz(i), "Fizz")

        for i in range(5,15,5):
            self.assertEqual(fizzbuzz(i), "Buzz")


if __name__ == '__main__':
    unittest.main()
