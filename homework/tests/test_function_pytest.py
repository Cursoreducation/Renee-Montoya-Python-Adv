import pytest
from functions_to_test import Calculator


def test_add_01():
    assert Calculator.add('2', '3') == '23'
    assert Calculator.add(-1, 1) == 0


def test_add_02():
    test = Calculator.add('2', '3')
    assert isinstance(test, str)
    test = Calculator.add(2.0, 3)
    assert isinstance(test, float)


def test_add_03():
    with pytest.raises(TypeError):
        Calculator.add('9', 8)


def test_subtract_01():
    assert Calculator.subtract(10, 4) == 6


def test_subtract_02():
    with pytest.raises(TypeError):
        Calculator.subtract('4', '5')


@pytest.mark.parametrize(
    ("a", "b", "c"), [
        (1, 9, 9),
        (-5, 5, -25),
        ("2", 3, "222"),
        (2, "2", "22")
    ]
)
def test_multiply_01(a, b, c):
    assert Calculator.multiply(a, b) == c


@pytest.mark.parametrize(
    ("a", "b", "c"), [
        (1, 1, int),
        (1.0, 1.0, float),
        ("1", 1, str),
    ]
)
def test_multiply_02(a, b, c):
    test = Calculator.multiply(a, b)
    assert isinstance(test, c)


def test_multiply_03():
    with pytest.raises(TypeError):
        Calculator.multiply('1', '7')


@pytest.mark.parametrize(
    ("a", "b", "c"), [
        (1, 1, 1),
        (-1, 1, -1),
        (-1, -1, 1),
        (0, 100000, 0)
    ]
)
def test_divide_01(a, b, c):
    assert Calculator.divide(a, b) == c


def test_divide_02():
    with pytest.raises(ValueError):
        Calculator.divide(1, 0)


@pytest.mark.parametrize(
    ("a", "b", "c"), [
        (1, 1.0, float),
        (1, 1.0, float),
        (1.0, 1.0, float)
    ]
)
def test_divide_03(a, b, c):
    test = Calculator.divide(a, b)
    assert isinstance(test, c)


def test_divide_04():
    with pytest.raises(TypeError):
        Calculator.divide('9', 9)
