import pytest
from functions_to_test import Calculator

def test_add():
    assert Calculator.add(2, 2) == 4

def test_subtract():
    assert Calculator.subtract(2, 2) == 0

def test_multiply():
    assert Calculator.multiply(2, 2) == 9

def test_divide():
    assert Calculator.divide(2, 2) == 0