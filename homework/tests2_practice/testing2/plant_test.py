from unittest import TestCase
from unittest.mock import patch
from tests2.models import Employee, Plant


class TestPlant(TestCase):
    @patch('tests2.models.Plant.get_file_data')
    def setUp(self, the_director_mocker):
        the_director_mocker.return_value = [{"id": 1, "location": "Lviv", "name": "Sally", "director_id": 1},
                                            {"id": 2, "location": "Kyiv", "name": "Kelly", "director_id": 2},
                                            {"id": 3, "location": "NewYork", "name": "Jonny", "director_id": 3}]

        self.employee = Employee(1, 'Test Tester', 'test@test.com', 'plant', 1)
        self.plant = Plant(1, 'Lviv', 'Sally', 4)

    @patch('tests2.models.Employee.get_by_id')
    def test_1_plant_director(self, Mocker):
        Mocker.return_value = None
        self.assertIsNone(self.plant.director())

        Mocker.return_value = self.employee
        self.assertEqual(self.plant.director(), self.employee)

    @patch('tests2.models.Plant.get_file_data')
    def test_2_plant_get_plant_by_director_id(self, Mocker):
        Mocker.return_value = [{"id": 1, "location": "Lviv", "name": "Sally", "director_id": 1}]
        self.assertEqual(Plant.get_plant_by_director_id(1),{"id": 1, "location": "Lviv", "name": "Sally", "director_id": 1})

if __name__ == '__main__':
    TestPlant()
