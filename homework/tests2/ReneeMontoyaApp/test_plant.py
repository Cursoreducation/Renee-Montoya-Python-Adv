# 2. Create test for Plant.director() and Plant.get_plant_by_director_id() methods
# You can use one of the following libraries:
#    Pytest
#    Unittest

from models import Plant, Employee

#
# @fixture()
# def plant():
#     return Plant(1, 'Kiev', "Test", 1)

def test_plant_save():
    plant = Plant(1, 'Kiev', "Test", 1)
    file = open('database/tests/test.json', 'w')
    file.write('[]')
    file.close()
    Plant.file = 'tests/test.json'
    plant.save()
    assert 'id' in plant.get_by_id(1)
    assert plant.name == plant.get_by_id(1)['name']