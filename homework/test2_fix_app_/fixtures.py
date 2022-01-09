from pytest import fixture
from models.models import Plant


@fixture()
def plant():
    return Plant(1, 'Kiev', "Test", 1)
