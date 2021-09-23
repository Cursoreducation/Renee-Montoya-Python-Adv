from models.plant import Plant
from fixtures import *


def test_plant_save(plant):
    plant.file = 'tests/test.json'
    plant.save()
    assert 'id' in plant.get_by_id(1)