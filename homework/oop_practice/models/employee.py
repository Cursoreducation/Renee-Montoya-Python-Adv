from oop_practice.framework.models import Model


class EmailErrorEmployee(Exception):
    pass


class Employee(Model):
    file = "employees.json"

    def __init__(self, id, name, email, department_type, department_id):
        self.id = id
        self.name = name
        self.email = email
        self.department_type = department_type
        self.department_id = department_id

    @classmethod
    def find_email(cls, email):
        for employee__ in cls.get_all():
            try:
                if employee__.email == email:
                    return employee__
                else:
                    raise EmailErrorEmployee("Email with employee haven't.")
            except EmailErrorEmployee:
                print("Email with employee haven't.")

    def __str__(self):
        return f"Employee(id: {self.id}", \
               f"name: {self.name}", \
               f"email: {self.email}", \
               f"department_type{self.department_type}", \
               f"department_id{self.department_id})"
