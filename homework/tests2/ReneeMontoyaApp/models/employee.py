from framework.models import Model
from plant import Plant


class Employee(Model):
    file = "employees.json"

    def __init__(self, id, name, email, department_type, department_id):
        self.id = id
        self.name = name
        self.email = email
        self.department_type = department_type
        self.department_id = department_id
        self.is_director = False
        if Plant.get_plant_by_director_id(self.id) is not None:
            self.is_director = True


    def department(self):
        if self.department_type == "plant":
            return Plant.get_by_id(self.deparment_id)
        return None



    def _generate_dict(self):
        return {
            'id': self.id,
            'email': self.email,
            'name': self.name,
            'department_type': self.department_type,
            'department_id': self.department_id
        }

    def save(self):
        employees_in_dict_format = self._generate_dict()
        employees = self.get_file_data(self.file)
        employees.append(employees_in_dict_format)
        try:
            element = self.get_by_id(self.id)
        except Exception:
            self.save_to_file(employees)
