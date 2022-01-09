from unittest import TestCase
from functions_to_test import Calculator


class TestCalculator(TestCase):
    def test_add_001(self):
        self.assertEqual(Calculator.add(-1, 1), 0)
        self.assertEqual(Calculator.add('1', '1'), '11')
        self.assertNotEqual(Calculator.add(1, 0), 0)
        self.assertIsInstance(Calculator.add(1, 1), int)
        self.assertIsInstance(Calculator.add(1, 1.0), float)
        self.assertIsInstance(Calculator.add('1', '1'), str)
        with self.assertRaises(TypeError):
            Calculator.add('1', 1)

    def test_subtract_002(self):
        self.assertEqual(Calculator.subtract(1, 1), 0)
        self.assertNotEqual(Calculator.subtract(1, 0), 0)
        self.assertIsInstance(Calculator.subtract(1, 1), int)
        self.assertNotIsInstance(Calculator.subtract(1.0, 1), int)
        with self.assertRaises(TypeError):
            Calculator.subtract('1', 1)

    def test_multiply_003(self):
        self.assertEqual(Calculator.multiply(1, 0), 0)
        self.assertNotEqual(Calculator.multiply(0, 1), 1)
        self.assertNotEqual(Calculator.multiply('0', 2), '0')
        self.assertNotEqual(Calculator.multiply(0, '2'), '0')
        self.assertIsInstance(Calculator.multiply(1, 1), int)
        self.assertIsInstance(Calculator.multiply('1', 2), str)
        with self.assertRaises(TypeError):
            Calculator.multiply('1', '1')

    def test_divide_004(self):
        self.assertEqual(Calculator.divide(1, 1), 1.0)
        self.assertNotEqual(Calculator.divide(0, 1), 1)
        self.assertIsInstance(Calculator.divide(1, 1), float)
        self.assertNotIsInstance(Calculator.divide(1, 1), int)
        with self.assertRaises(TypeError):
            Calculator.divide('1', 1)
        with self.assertRaises(ValueError):
            Calculator.divide(0, 0)


if __name__ == '__main__':
    TestCalculator()
