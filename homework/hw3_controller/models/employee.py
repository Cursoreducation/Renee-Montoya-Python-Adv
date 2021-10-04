from framework.models import Model


class Employee(Model):
    file = "employees.json"

    def __init__(self, id, name, email, department_type, department_id):
        self.id = id
        self.name = name
        self.email = email
        self.department_type = department_type
        self.department_id = department_id

    # def _generate_dict(self):
    #     return {
    #         'id': self.id,
    #         'email': self.email,
    #         'name': self.name,
    #         'department_type': self.department_type,
    #         'department_id': self.department_id
    #     }

    @classmethod
    def search_by_email(cls, email):
        for empl in cls.get_all():
            if empl.email == email:
                return empl
        raise Exception('Not found Employee')

    def __str__(self):
        return f'Emp(id={self.id}, email={self.email}, name={self.name}, ' \
               f'dep_type={self.department_type} dep_id={self.department_id})'
