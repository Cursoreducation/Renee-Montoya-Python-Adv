from framework.models import Model
from employee import Employee


class Plant(Model):
    file = "plants.json"

    def __init__(self, id, location, name, director_id):
        try:
            plant = self.get_by_id(id)
            self.id = id
            self.location = plant['location']
            self.name = plant['name']
            self.director_id = plant['director_id']
        except Exception:
            self.id = id
            self.location = location
            self.name = name
            self.director_id = director_id
            if self.director() is None:
                del self
                raise Exception("We don't have employee with this id!")

    def director(self):
        try:
            director = Employee.get_by_id(self.director_id)
            return director
        except Exception:
            return None

    @classmethod
    def get_plant_by_director_id(cls, director_id):
        plants = cls.get_file_data(cls.file)
        for plant in plants:
            if plant['director_id'] == director_id:
                return plant
        return None

    def _generate_dict(self):
        return {
            'id': self.id,
            'location': self.location,
            'name': self.name,
            'director_id': self.director_id
        }

    def save(self):
        plant_in_dict_format = self._generate_dict()
        plants = self.get_file_data(self.file)
        plants.append(plant_in_dict_format)
        try:
            element = self.get_by_id(self.id)
        except Exception:
            self.save_to_file(plants)
