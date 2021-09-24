from oop_practice.framework.models import Model


class Plant(Model):
    file = "plants.json"

    def __init__(self, id, location, name, director_id):
        self.id = id
        self.location = location
        self.name = name
        self.director_id = director_id

    def __str__(self):
        return f"Plant(id: {self.id}", \
               f"location: {self.location}", \
               f"name: {self.name}", \
               f"director_id{self.director_id})"
