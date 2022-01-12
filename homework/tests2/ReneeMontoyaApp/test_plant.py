from fixtures import *
from models import Plant, Employee
from mock import patch


def test_plant_save(plant):
    file = open('database/tests/test.json', 'w')
    file.write('[]')
    file.close()
    Plant.file = 'tests/tests.json'
    plant.save()
    assert 'id' in plant.get_by_id(1)
    assert plant.name == plant.get_by_id(1)['name']

@patch('models.Employee.get_by_id')
def test_plant_director(mock_data, plant):
    mock_data.return_value = {"id": 1, "email": "lubomur.luzhnuy@gmail.com", "name": "Liubomyr Luzhnyi", "department_type": "plant", "department_id": 1}
    assert plant.director() == {"id": 1, "email": "lubomur.luzhnuy@gmail.com", "name": "Liubomyr Luzhnyi", "department_type": "plant", "department_id": 1}

@patch('models.Employee.get_by_id')
def test_plant_director_empty(mock_data, plant):
    mock_data.return_value = None
    assert plant.director() is None

@patch('models.Plant.get_file_data')
def test_plant_get_by_director_id(mock_data, plant):
    mock_data.return_value = [{"id": 1, "location": "Lviv", "name": "Renee", "director_id": 1},
                              {"id": 2, "location": "Kiev", "name": "ReneeMantoya", "director_id": 2},
                              {"id": 4, "location": "Kk", "name": "Kk", "director_id": 3}]
    assert plant.get_plant_by_director_id(3) == {"id": 4, "location": "Kk", "name": "Kk", "director_id": 3}
    assert 'id' in plant.get_plant_by_director_id(3)

@patch('models.Plant.get_file_data')
def test_plant_get_by_director_id_empty(mock_data, plant):
    mock_data.return_value = []
    assert plant.get_plant_by_director_id(3) is None
