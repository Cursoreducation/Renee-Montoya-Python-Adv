import unittest
from functions_to_test import Calculator


class CalculatorTests(unittest.TestCase):
    """A sample Tests class"""

    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        res = self.calculator.add(2, 5)
        self.assertEqual(res, 7)

    def test_subtract(self):
        res = self.calculator.subtract(7, 5)
        self.assertEqual(res, 2)

    def test_multiply(self):
        res = self.calculator.multiply(5, 7)
        self.assertEqual(res, 35)

    def test_divide_raise(self):
        self.assertRaises(ValueError, lambda: self.calculator.divide(2, 0))

    def test_divide(self):
        res = self.calculator.divide(12, 4)
        self.assertEqual(res, 3)

import pytest

@pytest.fixture()
def calculator():
    calculator = Calculator()

def pytests_add(calculator):
    assert calculator.add(2, 5) == 7

def pytests_subtract(calculator):
    assert calculator.subtract(7, 5) == 2

def pytests_multiply(calculator):
    assert calculator.multiply(5, 7) == 35

def pytests_divide(calculator):
    assert calculator.divide(12, 4) == 3

def pytests_divide_by_zero(calculator):
    with pytest.raises(ValueError) as e:
        calculator.divide(2, 0)
    assert 'Can not divide by zero!' in str(e.value)

# if __name__ == "__main__":
#     unittest.main()

