import pytest
from functions_to_test import Calculator


def test_add():
    assert Calculator().add(8, 4) == 12


def test_subtract():
    assert Calculator().subtract(8, 4) == 4


def test_multiply():
    assert Calculator().multiply(8, 4) == 32


def test_divide():
    assert Calculator().divide(8, 4) == 2


def test_divide_by_zero():
    with pytest.raises(ValueError):
        Calculator().divide(8, 0)


if __name__ == '__main__':
    test_add()
    test_subtract()
    test_multiply()
    test_divide()
    test_divide_by_zero()
