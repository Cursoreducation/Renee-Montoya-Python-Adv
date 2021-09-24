from framework.models import Model


class Employee(Model):
    file = "employees.json"

    def __init__(self, id, name, email, department_type, department_id):
        self.id = id
        self.name = name
        self.email = email
        self.department_type = department_type
        self.department_id = department_id

    def search_id(self, email):
        employees = self.get_file_data(self.file)
        for el in employees:
            if el['email'] == email:
                return el['id']
        else:
            return 0
