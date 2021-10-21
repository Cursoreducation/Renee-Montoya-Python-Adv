import unittest
from functions_to_test import Calculator


class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calcTest = Calculator()

    def test_add(self):
        self.assertEqual(self.calcTest.add(8, 4), 12)

    def test_subtract(self):
        self.assertEqual(self.calcTest.subtract(8, 4), 4)

    def test_multiply(self):
        self.assertEqual(self.calcTest.multiply(8, 4), 32)

    def test_divide(self):
        self.assertEqual(self.calcTest.divide(8, 4), 2)
        self.assertRaises(ValueError, self.calcTest.divide, 8, 0)


if __name__ == '__main__':
    unittest.main()
