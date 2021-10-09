import unittest
# from unittest.mock import patch
from employee import Employee


class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.employee = Employee("Volodymyr", "Salitrynskyi", 5)

    def test_email(self):
        self.assertEqual(self.employee.email(),
                         "Volodymyr.Salitrynskyi@email.com")

    def test_fullname(self):
        self.assertEqual(self.employee.fullname(), "Volodymyr Salitrynskyi")

    def test_apply_raise(self):
        self.assertEqual(self.employee.apply_raise(), 5)


if __name__ == '__main__':
    unittest.main()
