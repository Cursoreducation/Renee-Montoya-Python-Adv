from pytest import fixture
from models import Plant


@fixture()
def plant():
    return Plant(1, 'Lviv', "Test", 1)
