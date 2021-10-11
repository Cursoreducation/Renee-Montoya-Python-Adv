import unittest
from unittest.mock import patch

from ReneeMontoyaApp.models import Plant, Employee


class TestPlant(unittest.TestCase):

    @patch('ReneeMontoyaApp.models.Plant.get_file_data')
    def setUp(self, plant_director_mock):
        plant_director_mock.return_value = [{"id": 1, "location": "Lviv", "name": "Renee", "director_id": 1},
                                            {"id": 2, "location": "Kiev", "name": "ReneeMantoya", "director_id": 2},
                                            ]
        self.employee1 = Employee(1, 'Test Tester', 'test@test.com', 'plant', 1)
        self.plant1 = Plant(1, 'Lviv', 'Renee', 2)

    @patch('ReneeMontoyaApp.models.Employee.get_by_id')
    def test_director_empty(self, plantMock):
        plantMock.return_value = None
        self.assertIsNone(self.plant1.director())

    @patch('ReneeMontoyaApp.models.Employee.get_by_id')
    def test_director(self, plantMock):
        plantMock.return_value = self.employee1
        self.assertEqual(self.plant1.director(), self.employee1)

    @patch('ReneeMontoyaApp.models.Plant.get_file_data')
    def test_department(self, plantMock):
        plantMock.return_value = [{"id": 1, "location": "Lviv", "name": "Renee", "director_id": 1},
                                  {"id": 2, "location": "Kiev", "name": "ReneeMantoya", "director_id": 2},
                                  {"id": 4, "location": "Kk", "name": "Kk", "director_id": 1}]
        self.assertEqual(Plant.get_plant_by_director_id(2), {"id": 2, "location": "Kiev", "name": "ReneeMantoya", "director_id": 2})
