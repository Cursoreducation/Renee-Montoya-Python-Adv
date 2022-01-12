from framework.models import Model


class Plant(Model):
    file = "plants.json"

    def __init__(self, id, location, name, director_id):
        self.id = id
        self.location = location
        self.name = name
        self.director_id = director_id

    # def _generate_dict(self):
    #     return {
    #         'id': self.id,
    #         'location': self.location,
    #         'name': self.name,
    #         'director_id': self.director_id
    #     }
    #
    # def save(self):
    #     plant_in_dict_format = self._generate_dict()
    #     plants = self.get_file_data(self.file)
    #     plants.append(plant_in_dict_format)
    #     self.save_to_file(plants)
