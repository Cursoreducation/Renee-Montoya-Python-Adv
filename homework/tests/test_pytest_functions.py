import unittest
from functions_to_test import Calculator

class TestFunctions(unittest.TestCase):

    def setUp(self):
        self.classTest = Calculator()

    def test_substract(self):
        self.assertEqual(self.classTest.subtract(2, 1), 1)

    def test_sum(self):
        self.assertEqual(self.classTest.add(2, 1), 3)


    def test_multiply(self):
        self.assertEqual(self.classTest.multiply(2, 1), 2)

    def test_divide(self):
        self.assertEqual(self.classTest.divide(2, 1), 2)

    def test_divide_zero(self):
        self.assertRaises(ValueError, self.classTest.divide, 2, 0)

