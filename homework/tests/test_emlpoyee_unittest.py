import unittest
from unittest.mock import patch
from employee import Employee
import requests
import requests_mock


class TestEmployee(unittest.TestCase):

    def setUp(self) -> None:
        self.user = Employee('Solka', 'Abc', 2000)

    def test_first(self):
        self.assertEqual(self.user.first, 'Solka')

    def test_last(self):
        self.assertEqual(self.user.last, 'Abc')

    def test_pay(self):
        self.assertEqual(self.user.pay, 2000)

    def test_email(self):
        self.assertEqual(self.user.email, 'Solka.Abc@email.com')

    def test_fullname(self):
        self.assertEqual(self.user.fullname, 'Solka Abc')

    def test_apply_raise(self):
        self.user.apply_raise()
        self.assertEqual(self.user.pay, 2100)

    @patch('employee.requests.get')
    def test_monthly_schedule_01(self, mocker):
        mocker.return_value.ok = True
        mocker.return_value.text = 'data monthly schedule for July'
        self.assertEqual(self.user.monthly_schedule('July'), 'data monthly schedule for July')

    @patch('employee.requests.get')
    def test_monthly_schedule_02(self, mocker):
        mocker.return_value.ok = False
        mocker.return_value.text = 'data monthly schedule for July'
        self.assertEqual(self.user.monthly_schedule('July'), 'Bad Response!')
