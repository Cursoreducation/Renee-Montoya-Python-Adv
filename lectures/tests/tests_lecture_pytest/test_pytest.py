from functions import *
from classes import *
from fixtures import *


def test_check_sum():
    assert check_sum(2, 5) == 7


def test_after_check_sum(mocker, some_data):
    mocker.patch("functions.check_sum", return_value=some_data)
    assert check_after_sum(5, 7) == 0


def test_list():
    assert 2 in r_list()


def test_get_operating_system(mocker):
    mocker.patch("functions.is_windows", return_value=True)
    assert get_operating_system() == "Windows"


def test_request(requests_mock):
    requests_mock.get(
        "http://jsonplaceholder.typicode.com/tsodos", text="data", status_code=200
    )
    classForTest = ClassForTest()
    assert classForTest.send_request().ok
    assert classForTest.send_request().status_code == 200


def test_fixture(some_data):
    assert some_data == 0
