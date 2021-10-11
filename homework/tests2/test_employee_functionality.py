import unittest
from unittest.mock import patch

from ReneeMontoyaApp.models import Employee, Plant


class TestEmployee(unittest.TestCase):
    @patch('ReneeMontoyaApp.models.Plant.get_file_data')
    def setUp(self, plant_director_mock):
        plant_director_mock.return_value = [{"id": 1, "location": "Lviv", "name": "Renee", "director_id": 1},
                                            {"id": 2, "location": "Kiev", "name": "ReneeMantoya", "director_id": 2},
                                            {"id": 4, "location": "Kk", "name": "Kk", "director_id": 1}]
        self.plant = Plant.get_by_id(1)
        self.employee1 = Employee(1, 'Test Tester', 'test@test.com', 'plant', 1)
        self.employee2 = Employee(2, 'Test Tester', 'test@test.com', 'other', 1)

    @patch('ReneeMontoyaApp.models.Plant.get_by_id')
    def test_empty_department(self, plantMock):
        plantMock.return_value = None
        self.assertIsNone(self.employee2.department())

    @patch('ReneeMontoyaApp.models.Plant.get_by_id')
    def test_get_plant_by_director_id(self, plantMock):
        plantMock.return_value = self.plant
        self.assertEqual(self.employee1.department(), self.plant)
