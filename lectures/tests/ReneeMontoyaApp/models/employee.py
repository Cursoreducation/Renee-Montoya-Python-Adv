from framework.models import Model


class Employee(Model):
    file = "employees.json"

    def __init__(self, id, name, email, department_type, department_id):
        self.id = id
        self.name = name
        self.email = email
        self.department_type = department_type
        self.department_id = department_id

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
