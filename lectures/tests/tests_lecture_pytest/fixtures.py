import pytest


@pytest.fixture()
def some_data():
    return 0


@pytest.fixture()
def user():
    return {
        "id": 1,
        "username": "vinni_puch",
        "email": "turupuru8@gmail.com",
    }
