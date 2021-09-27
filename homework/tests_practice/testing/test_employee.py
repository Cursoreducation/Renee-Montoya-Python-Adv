from tests.employee import Employee
import pytest
from unittest import TestCase
from unittest.mock import patch


@pytest.fixture()
def user():
    print("Denzel")


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

    def setUp(self):
        self.employee = Employee("Jack", "Sallivan", 200)

    def test_check_first_name_01(self):
        self.assertEqual(self.employee.first, "Jack")

    def test_check_first_name_02(self):
        self.assertNotEqual(self.employee.first, "John")

    def test_check_last_name_03(self):
        self.assertEqual(self.employee.last, "Sallivan")

    def test_check_last_name_04(self):
        self.assertNotEqual(self.employee.last, "Sally")

    def test_check_correct_pay_05(self):
        self.assertEqual(self.employee.pay, 200)

    def test_property_email_06(self):
        self.assertEqual(self.employee.email, 'Jack.Sallivan@email.com')
        self.employee.first = "Denzel"
        self.employee.last = "Rayan"
        self.assertEqual(self.employee.email, 'Denzel.Rayan@email.com')

    def test_property_fullname_07(self):
        self.employee.first = "Arnold"
        self.employee.last = "Schwerzer"
        self.assertEqual(self.employee.fullname, 'Arnold Schwerzer')

    def test_apply_raise_08(self):
        self.employee.apply_raise()
        self.assertNotEqual(self.employee.pay, 209)
        self.assertEqual(self.employee.pay, 210)

    @patch('requests.get')
    def test_false_monthly_schedule_09(self, mocker_):
        class MockerFalse():
            ok = False
            text = "Arnold Schwerzer"

        mocker_.return_value = MockerFalse()
        self.assertEqual(self.employee.monthly_schedule(1), 'Bad Response!')

    @patch('requests.get')
    def test_monthly_schedule_10(self, mocker):
        class Mocker():
            ok = True
            text = "Arnold Schwerzer"

        mocker.return_value = Mocker()
        self.assertEqual(self.employee.monthly_schedule(10), "Arnold Schwerzer")


if __name__=="__main__":
    user()
    TestEmployee()
