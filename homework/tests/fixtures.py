from pytest import fixture
from employee import Employee


@fixture()
def employ():
    return Employee('Solka', 'Abc', 1000)
