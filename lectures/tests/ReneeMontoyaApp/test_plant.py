from fixtures import *
from models import Plant

def test_plant_save(plant):
    file = open('database/tests/test.json', 'w')
    file.write('[]')
    file.close()
    Plant.file = 'tests/tests.json'
    plant.save()
    assert 'id' in plant.get_by_id(1)
    assert plant.name == plant.get_by_id(1)['name']