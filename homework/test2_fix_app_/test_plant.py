import unittest
from unittest.mock import patch
from models.models import Plant, Employee


class TestPlant(unittest.TestCase):
    @patch('models.models.Plant.get_file_data')
    def setUp(self, plant_director_mock):
        plant_director_mock.return_value = [{"id": 1, "location": "IF", "name": "IFAZ", "director_id": 101},
                                            {"id": 2, "location": "Lviv", "name": "LAZ", "director_id": 102},
                                            {"id": 3, "location": "Kyiv", "name": "KAZ", "director_id": 103}
                                            ]
        self.employee1 = Employee(1, 'Cool Boss', 'cool-boss@mail.com', 'plant', 1)
        self.plant1 = Plant(1, 'IF', 'IFAZ', 101)

    @patch('models.models.Employee.get_by_id')
    def test_director_empty(self, plant_mock):
        plant_mock.return_value = None
        self.assertIsNone(self.plant1.director())

    @patch('models.models.Employee.get_by_id')
    def test_director_not_empty(self, plant_mock):
        plant_mock.return_value = self.employee1
        self.assertEqual(self.plant1.director(), self.employee1)

    @patch('models.models.Plant.get_file_data')
    def test_get_plant_by_director_id(self, plant_mock):
        plant_mock.return_value = [{"id": 1, "location": "IF", "name": "IFAZ", "director_id": 101},
                                   {"id": 2, "location": "Lviv", "name": "LAZ", "director_id": 102},
                                   {"id": 3, "location": "Kyiv", "name": "KAZ", "director_id": 103}]
        self.assertEqual(Plant.get_plant_by_director_id(102),
                         {"id": 2, "location": "Lviv", "name": "LAZ", "director_id": 102})

    # def test_plant_save(self):
    #     # ReneeMontoyaApp_from_fix/database/tests/test.json
    #     file = open('ReneeMontoyaApp_from_fix/database/tests/test.json', 'w')
    #     file.write('[]')
    #     file.close()
    #     Plant.file = 'ReneeMontoyaApp_from_fix/database/tests/test.json'
    #     self.save()
    #     assert 'id' in self.get_by_id(1)
    #     assert self.name == self.get_by_id(1)['name']
