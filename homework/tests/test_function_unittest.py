import unittest
from functions_to_test import Calculator


class TestFunctions(unittest.TestCase):
    def test_add(self):
        self.assertEqual(Calculator.add(2, 3), 5)
        self.assertRaises(TypeError, Calculator.add, 2, '3')
        self.assertEqual(Calculator.add('2', '3'), '23')

    def test_subtract(self):
        self.assertEqual(Calculator.subtract(2, 3), -1)

    def test_multiply(self):
        self.assertEqual(Calculator.multiply(2, 3), 6)
        self.assertRaises(TypeError, Calculator.multiply, '2', '3')
        self.assertEqual(Calculator.multiply('2', 3), '222')

    def test_divide(self):
        self.assertRaises(ValueError, Calculator.divide, 2, 0)
        self.assertEqual(Calculator.divide(6, 3), 2)
        self.assertIsInstance(Calculator.divide(6, 3), float)



