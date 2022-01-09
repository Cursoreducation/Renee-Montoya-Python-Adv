import unittest
from unittest.mock import patch
import requests
import requests_mock

from employee import Employee


class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.employ = Employee('Jho', 'Mantius', 500)

    def test_first_name(self):
        self.assertEqual(self.employ.first, 'Jho')

    def test_last_name(self):
        self.assertEqual(self.employ.last, "Mantius")

    def test_pay(self):
        self.assertEqual(self.employ.pay, 500)

    def test_email(self):
        self.assertEqual(self.employ.email, "Jho.Mantius@email.com")

    def test_fullname(self):
        self.assertEqual(self.employ.fullname, "Jho Mantius")

    def test_apply_raise(self):
        self.employ.apply_raise()
        self.assertEqual(self.employ.pay, 525)

    @patch('requests.get')
    def test_monthly_schedule(self, mocker):
        class MyMock():
            ok = True
            text = '4,8,16,27 September'

        mocker.return_value = MyMock()
        self.assertEqual(self.employ.monthly_schedule(9), '4,8,16,27 September')

if __name__ == '__main__':
    unittest.main()



