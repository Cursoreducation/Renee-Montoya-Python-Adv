from employee import Employee
import unittest
from unittest.mock import patch


class EmployeeTests(unittest.TestCase):
    def setUp(self):
        self.empl = Employee('Nikita', 'Krutoholov', 1000)

    def test_email_property(self):
        self.assertEqual(self.empl.email, 'Nikita.Krutoholov@email.com')

    def test_fullname_property(self):
        self.assertEqual(self.empl.fullname, 'Nikita Krutoholov')

    def test_apply_raise(self):
        self.empl.apply_raise()
        self.assertEqual(self.empl.pay, 1050)

    @patch('employee.requests.get')
    def test_monthly_schedule(self, mocked_get):
        mocked_get.return_value.ok = True
        res = self.empl.monthly_schedule('august')
        self.assertIsNotNone(res)
        self.assertNotEqual(res, 'Bad Response!')

if __name__ == "__main__":
    unittest.main()
