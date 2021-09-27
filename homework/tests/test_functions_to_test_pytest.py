import pytest
from functions_to_test import Calculator


def test_add():
    assert Calculator.add(2, 2) == 4


def test_subtract():
    assert Calculator.subtract(8, 2) == 6


def test_multiply():
    assert Calculator.multiply(3, 3) == 9


def test_divide():
    assert Calculator.divide(10, 2) == 5
    # with pytest.raises(ZeroDivisionError):
    # Calculator.divide(1/0)
    if "y" == 0:
        raise ValueError('Can not divide by zero!')
