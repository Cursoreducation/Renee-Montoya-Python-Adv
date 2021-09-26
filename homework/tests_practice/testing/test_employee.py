import unittest
from tests.employee import Employee
from unittest import TestCase
import pytest


@pytest.fixture()
def user():
     print("Jack")


@pytest.mark.usefixtures("user")
@pytest.mark.parametrize("first, last, pay", [(100, 200, 300)])
def test_1(first, last, pay):
    employee = Employee(100, 200, 300)
    employee.first = first
    employee.last = last
    employee.pay = pay
    assert employee.first != last
    assert employee.first == first
    assert employee.last == last


class TestEmployee(TestCase):

    @unittest.skip(reason="skip")
    def test_email_2(self):
        employee_ = Employee("john", 'recon',50)
        employee_.email = "jack", "salivan"
        self.assertIn("jack", (employee_.email()))

CONSTANT = False


@pytest.mark.skipif(CONSTANT is False, reason="skip")
def test_monthly_schedule_3(requests_mock):
    requests_mock.get(
        "http://jsonplaceholder.typicode.com/tsodos", text="data", status_code=200
    )
    classForTest = Employee("jack", "salivan", 50)
    assert classForTest.monthly_schedule(2).ok
    assert classForTest.monthly_schedule(2).status_code == 200


if __name__=="__main__":
    TestEmployee()
    user()
