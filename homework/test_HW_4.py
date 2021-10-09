import unittest
from functions_to_test import Calculator

class TestCalculator(unittest.TestCase):
    def test_add(self):
        a = Calculator()
        result = a.add(2,2)
        self.assertEqual(result, 4)

class TestCalculator(unittest.TestCase):
    def test_multiply(self):
        a = Calculator()
        result = a.multiply(2,2)
        self.assertEqual(result, 4)

class TestCalculator(unittest.TestCase):
    def test_subtract(self):
        a = Calculator()
        result = a.subtract(2,2)
        self.assertEqual(result, 0)

class TestCalculator(unittest.TestCase):
    def test_division(self):
        a = Calculator()
        result = a.division(2,2)
        self.assertEqual(result, 1)