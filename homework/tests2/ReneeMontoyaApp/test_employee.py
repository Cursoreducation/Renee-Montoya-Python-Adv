import unittest
from unittest.mock import patch
from models import Employee, Plant


class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.employee = Employee(1, 'Test Tester', 'test@test.com', 'plant', 1)
        self.deparment_type = 'plant'

    def test_generate_dict(self):
        self.assertIn('id', self.employee._generate_dict())
        self.assertEqual(self.employee._generate_dict()['id'], 1)
        self.assertEqual(self.employee._generate_dict()['department_type'], 'plant')

    @patch('models.Employee.get_file_data')
    def test_get_by_id(self, fileDataMock):
        fileDataMock.return_value = [{"id": 1, "email": "lubomur.luzhnuy@gmail.com", "name": "Liubomyr Luzhnyi", "department_type": "plant", "department_id": 1}, {"id": 2, "email": "anton@gmail.com", "name": "Anton", "department_type": "plant", "department_id": 2}]
        self.assertEqual(self.employee.get_by_id(1)['email'], "lubomur.luzhnuy@gmail.com")
        self.assertIn('id', self.employee.get_by_id(1))

    @patch('models.Plant.get_by_id')
    def test_department(self, data_mock):
        plant = {"id": 1, "location": "Lviv", "name": "Renee", "director_id": 1}
        data_mock.return_value = plant
        self.assertEqual(self.employee.department(), plant)
        self.assertEqual(Plant.get_plant_by_director_id(1), plant)



