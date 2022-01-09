from framework.models import Model
from models.employee import Employee


class Plant(Model):
    file = "plants.json"

    def __init__(self, id_plant, location, name, director_id):
        self.id = id_plant
        self.location = location
        self.name = name
        self.director_id = director_id

    @classmethod
    def _set_dict(cls, self):
        return {'id': self.id,
                'location': self.location,
                'name': self.name,
                'director_id': self.director_id}

    @staticmethod
    def get_employee_class():
        return Employee.__name__

    @staticmethod
    def get_by_email(email):
        data_employees = Employee.get_file_data(Employee.file)
        for el in data_employees:
            if el['email'] == email:
                # return el["id"]
                return el
        raise Exception("Not found")
