import unittest
from unittest.mock import patch
from models import Employee


class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.employee = Employee(1, 'Test Tester', 'tests@tests.com', 'plant', 1)

    def test_generate_dict(self):
        self.assertIn('id', self.employee._generate_dict())
        self.assertEqual(self.employee._generate_dict()['id'], 1)
        self.assertEqual(self.employee._generate_dict()['department_type'], 'plant')

    @patch('models.Employee.get_file_data')
    def test_get_by_id(self, fileDataMock):
        fileDataMock.return_value = [{"id": 1, "email": "lubomur.luzhnuy@gmail.com", "name": "Liubomyr Luzhnyi", "department_type": "plant", "department_id": 1}, {"id": 2, "email": "anton@gmail.com", "name": "Anton", "department_type": "plant", "department_id": 2}]
        self.assertEqual(self.employee.get_by_id(1)['email'], "lubomur.luzhnuy@gmail.com")
        self.assertIn('id', self.employee.get_by_id(1))
