import unittest
from functions_to_test import Calculator


class TestFunctions(unittest.TestCase):
    def test_add(self):
        result = Calculator.add(1, 2)
        self.assertEqual(result, 3)

    def test_subtract(self):
        self.assertEqual(Calculator.subtract(4, 2), 2)

    def test_multiply(self):
        self.assertEqual(Calculator.multiply(4, 2), 8)

    def test_division(self):
        self.assertRaises(ValueError, lambda: Calculator.divide(2, 0))

        self.assertEqual(Calculator.divide(6, 3), 2)


if __name__ == '__main__':
    unittest.main()
