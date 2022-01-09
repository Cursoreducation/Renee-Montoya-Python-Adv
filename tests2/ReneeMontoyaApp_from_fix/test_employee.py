import unittest
from unittest.mock import patch
from ReneeMontoyaApp_from_fix.models.models import Employee, Plant


class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.plant = Plant.get_by_id(1)
        self.employee = Employee(1, 'Test Tester', 'test@test.com', 'plant', 1)

    def test_generate_dict(self):
        self.assertIn('id', self.employee._generate_dict())
        self.assertEqual(self.employee._generate_dict()['id'], 1)
        self.assertEqual(self.employee._generate_dict()['department_type'], 'plant')

    @patch('ReneeMontoyaApp_from_fix.models.models.Employee.get_file_data')
    def test_get_by_id(self, file_data_mock):
        file_data_mock.return_value = [{"id": 1, "email": "lubomur.luzhnuy@gmail.com", "name": "Liubomyr Luzhnyi",
                                        "department_type": "plant", "department_id": 1},
                                       {"id": 2, "email": "anton@gmail.com", "name": "Anton",
                                        "department_type": "plant", "department_id": 2}]
        self.assertEqual(self.employee.get_by_id(1)['email'], "lubomur.luzhnuy@gmail.com")
        self.assertIn('id', self.employee.get_by_id(1))

    @patch('ReneeMontoyaApp_from_fix.models.models.Plant.get_by_id')
    def test_employee_department_is_none(self, plant_mock):
        plant_mock.return_value = None
        self.assertIsNone(self.employee.department())

    @patch('ReneeMontoyaApp_from_fix.models.models.Plant.get_by_id')
    def test_get_plant_by_director_id(self, plant_mock):
        plant_mock.return_value = self.plant
        self.assertEqual(self.employee.department(), self.plant)
