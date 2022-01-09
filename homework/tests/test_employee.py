import unittest
from unittest.mock import patch
from employee import *


class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.user = Employee("Alex", "Lys", 26)

    def test_first(self):
        self.assertEqual(self.user.first, 'Alex')

    def test_last(self):
        self.assertEqual(self.user.last, 'Lys')

    def test_email(self):
        self.assertEqual(self.user.email, "Alex.Lys@email.com")

    def test_fullname(self):
        self.assertEqual(self.user.fullname, "Alex Lys")

    def test_apply_raise(self):
        self.user.apply_raise()
        self.assertEqual(self.user.pay, 27)

    @patch('requests.get')
    def test_monthly_schedule_true(self, mocker):
        class MockerUrl:
            ok = True
            text = "data of September month"

        mocker.return_value = MockerUrl()
        self.assertEqual(self.user.monthly_schedule(9), "data of September month")

    @patch('requests.get')
    def test_monthly_schedule_false(self, mocker):
        class MockerUrl:
            ok = False
            text = "data of September month"

        mocker.return_value = MockerUrl()
        self.assertEqual(self.user.monthly_schedule(9), "Bad Response!")


if __name__ == '__main__':
    unittest.main()
