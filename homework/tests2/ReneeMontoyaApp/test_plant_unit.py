import unittest
from unittest.mock import patch
from models import Plant, Employee


class TestPlant(unittest.TestCase):

    @patch('models.Plant.get_file_data')
    def setUp(self, mock_get_file_data):
        mock_get_file_data.return_value = [{"id": 1, "location": "Kiev", "name": "Zavod", "director_id": 1},
                              {"id": 2, "location": "Testcity", "name": "Tester", "director_id": 2}, ]

        self.employee_ = Employee(1, 'Test', 'test@test', 'plant', 1)
        self.plant = Plant(1, 'Kiev', 'Zavod', 1)

    @patch('models.Employee.get_by_id')
    def test_director_01(self, mock_get_by_id):
        mock_get_by_id.return_value = self.employee_
        self.assertEqual(self.plant.director(), self.employee_)

    @patch('models.Employee.get_by_id')
    def test_director_02(self, mock_get_by_id):
        mock_get_by_id.return_value = Exception
        self.assertRaises(self.plant.director())

    @patch('models.Employee.get_by_id')
    def test_director_03(self, mock_get_by_id):
        mock_get_by_id.return_value = None
        self.assertIsNone(self.plant.director())

    @patch('models.Plant.get_file_data')
    def test_director_by_id(self, mock_get_file_data):
        mock_get_file_data.return_value = [{"id": 2, "location": "Testcity", "name": "Tester", "director_id": 2}]
        self.assertEqual(Plant.get_plant_by_director_id(2),
                         {"id": 2, "location": "Testcity", "name": "Tester", "director_id": 2})
