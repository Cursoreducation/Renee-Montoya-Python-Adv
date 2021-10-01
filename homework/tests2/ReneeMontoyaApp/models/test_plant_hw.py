import unittest
from unittest.mock import patch

from models import Plant, Employee


class TestPlant(unittest.TestCase):

    @patch('models.Plant.get_file_data')
    def setUp(self, mock_get_file_data):
        mock_get_file_data.return_value = [{"id": 1, "location": "Lutsk", "name": "Jho", "director_id": 1},
                              {"id": 2, "location": "Lviv", "name": "Bob", "director_id": 2}, ]

        self.employee_ = Employee(1, 'Bob', 'kit@gmail.com', 'plant', 1)
        self.plant_ = Plant(1, 'Lutsk', 'Jho', 1)

    @patch('models.Employee.get_by_id')
    def test_director(self, mock_get_by_id):
        mock_get_by_id.return_value = self.employee_
        self.assertEqual(self.plant_.director(), self.employee_)

    @patch('models.Employee.get_by_id')
    def test_director_exception(self, mock_get_by_id):
        mock_get_by_id.return_value = Exception
        self.assertRaises(self.plant_.director())

    @patch('models.Plant.get_file_data')
    def test_director_by_id(self, mock_get_file_data):
        mock_get_file_data.return_value = [{"id": 1, "location": "Lutsk", "name": "Jho", "director_id": 1},
                                           {"id": 2, "location": "Lviv", "name": "Bob", "director_id": 2}, ]
        self.assertEqual(Plant.get_plant_by_director_id(2),
                         {"id": 2, "location": "Lviv", "name": "Bob", "director_id": 2})
