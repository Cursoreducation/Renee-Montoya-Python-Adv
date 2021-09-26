import pytest
from tests.functions_to_test import Calculator


@pytest.fixture()
def test_fixtures():
    print("setUp")
    user = "Jack"
    yield user
    print("tearDown")


def test_add_01(test_fixtures):
    print(test_fixtures)
    assert Calculator.add(50, 150) == 200
    assert Calculator.add(50, 50) == 100


@pytest.mark.usefixtures('test_fixtures')
def test_subtract_02():
    assert Calculator.subtract(120, 20) == 100

CONSTANT = True


@pytest.mark.skipif(CONSTANT is True, reason="skip")
def test_skip_03():
    assert Calculator.subtract(120, 20) == 80


@pytest.mark.parametrize(
    ("x", "y", "z"), [
        (10, 5, 50),
        (20, 3, 60),
        (40, 2, 80)
    ]
)
def test_multiply_04(x, y, z):
    assert Calculator.multiply(x, y) == z


@pytest.mark.parametrize(
    ("x", "y", "z"), [
        (100, 20, 5),
        (1800, 60, 30),
        (400, 2, 200)
    ]
)
def test_divide_05(x, y, z):
    assert Calculator.divide(x, y) == z


""" Instruction. For a check the results of tests run command in terminal: 
    'pytest tests/py_test.py'(*depend from location directory)
    or run file with method: '__name__=='__main__' which below."""

if __name__ == "__main__":
    test_fixtures()
