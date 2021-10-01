from unittest import TestCase
from unittest.mock import patch
from tests2.models import Employee, Plant


class TestEmployee(TestCase):
    @patch('tests2.models.Plant.get_file_data')
    def setUp(self, the_director_of_plant_mocker):
        self.employee = Employee(1, 'Test Tester', 'test@test.com', 'plant', 1)
        self.employee_2 = Employee(2, 'Test_2 Tester', 'test_2@test.com', 'enterprise', 2)
        the_director_of_plant_mocker.return_value = [{"id": 1, "location": "Lviv", "name": "Sally", "director_id": 1},
                                                     {"id": 2, "location": "Kyiv", "name": "Kelly", "director_id": 2},
                                                     {"id": 3, "location": "NewYork", "name": "Jonny", "director_id": 3}]
        self.plant = Plant.get_by_id(1)

    @patch('tests2.models.Plant.get_by_id')
    def test_1_none_department(self, none_Mocker):
        none_Mocker.return_value = None
        self.assertIsNone(self.employee_2.department())

    @patch('tests2.models.Plant.get_by_id')
    def test_2_department_with_value(self, value_Mocker):
        value_Mocker.return_value = 'plant'
        self.assertIsNotNone(self.employee.department_id)

if __name__ == '__main__':
    TestEmployee()
