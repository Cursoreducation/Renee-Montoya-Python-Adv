import pytest
from functions_to_test import Calculator


# Testing func "add"
@pytest.mark.parametrize(
    ("a", "b", "c"), [
        (1, 1, 2),
        (-1, 1, 0),
        (-1, -1, -2),
        ("1", "1", "11")
    ]
)
def test_add_010(a, b, c):
    assert Calculator.add(a, b) == c


@pytest.mark.parametrize(
    ("a", "b", "c"), [
        (1, 1, int),
        (1, 1.0, float),
        (1.0, 1.0, float),
        ("1", "1", str)
    ]
)
def test_add_011(a, b, c):
    test_add = Calculator.add(a, b)
    assert isinstance(test_add, c)


@pytest.mark.parametrize(
    ("a", "b"), [
        ("1", 1),
        (1, "1")
    ]
)
def test_add_012(a, b):
    with pytest.raises(TypeError):
        Calculator.add(a, b)


# Testing func "subtract"
@pytest.mark.parametrize(
    ("a", "b", "c"), [
        (1, 1, 0),
        (-1, 1, -2),
        (-1, -1, 0)
    ]
)
def test_subtract_020(a, b, c):
    assert Calculator.subtract(a, b) == c


@pytest.mark.parametrize(
    ("a", "b", "c"), [
        (1, 1, int),
        (2, 1.0, float),
        (2.0, 1.0, float)
    ]
)
def test_subtract_021(a, b, c):
    test_subtract = Calculator.subtract(a, b)
    assert isinstance(test_subtract, c)


@pytest.mark.parametrize(
    ("a", "b"), [
        ("1", 1),
        ("1", "1"),
        (1, "1")
    ]
)
def test_subtract_022(a, b):
    with pytest.raises(TypeError):
        Calculator.subtract(a, b)


# Testing func "multiply"
@pytest.mark.parametrize(
    ("a", "b", "c"), [
        (1, 1, 1),
        (-1, 1, -1),
        (-1, -1, 1),
        ("1", 2, "11"),
        (2, "2", "22")
    ]
)
def test_multiply_030(a, b, c):
    assert Calculator.multiply(a, b) == c


@pytest.mark.parametrize(
    ("a", "b", "c"), [
        (1, 1, int),
        (2, 1.0, float),
        (2.0, 1.0, float),
        ("1", 2, str),
        (2, "2", str)
    ]
)
def test_multiply_031(a, b, c):
    test_multiply = Calculator.multiply(a, b)
    assert isinstance(test_multiply, c)


@pytest.mark.parametrize(
    ("a", "b"), [
        ("1", "1")
    ]
)
def test_multiply_032(a, b):
    with pytest.raises(TypeError):
        Calculator.multiply(a, b)


# Testing func "divide"
@pytest.mark.parametrize(
    ("a", "b", "c"), [
        (1, 1, 1),
        (-1, 1, -1),
        (-1, -1, 1),
        (0, 100000, 0)
    ]
)
def test_divide_040(a, b, c):
    assert Calculator.divide(a, b) == c


def test_divide_041():
    with pytest.raises(ValueError):
        Calculator.divide(1, 0)


@pytest.mark.parametrize(
    ("a", "b"), [
        (1, 1),
        (2, 1.0),
        (2.0, 1.0)
    ]
)
def test_divide_042(a, b):
    test_divide = Calculator.divide(a, b)
    assert isinstance(test_divide, float)


@pytest.mark.parametrize(
    ("a", "b"), [
        ("1", "1"),
        (1, "1"),
        ("1", 1)
    ]
)
def test_divide_043(a, b):
    with pytest.raises(TypeError):
        Calculator.divide(a, b)
