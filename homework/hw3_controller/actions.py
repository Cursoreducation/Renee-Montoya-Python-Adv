from abc import ABC, abstractmethod

from models.employee import Employee
from models.plant import Plant


class BaseAction(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def execute(self):
        pass

    def get_action_name(self):
        return self.name


class AddNewPlantAction(BaseAction):

    def __init__(self):
        super().__init__('Add new Plant')

    def execute(self):
        try:
            id = int(input("ID: "))
        except ValueError:
            print('Only integer value is allowed!')
            return
        try:
            plant = Plant.get_by_id(id)
            print(f'Plant with id={id} and name={plant["name"]} - already exists')
        except Exception as _:
            location = input("Location: ")
            name = input("Name: ")
            # director_id = int(input("Director ID: "))
            email = input('Director E-Mail: ')
            try:
                empl = Employee.search_by_email(email)
            except Exception as _:
                print('Email not Found')
                return
            plant = Plant(id, location, name, empl.id)
            plant.save()


class AddNewEmployeeAction(BaseAction):

    def __init__(self):
        super().__init__('Add new Employee')

    def execute(self):
        id = int(input("ID: "))
        name = input("Name: ")
        email = input("Email: ")
        department_type = input("Department Type: ")
        department_id = int(input("Department id: "))
        employee = Employee(id, name, email, department_type, department_id)
        employee.save()


class GetEmployeeByIdAction(BaseAction):

    def __init__(self):
        super().__init__('Get employee by id')

    def execute(self):
        id = int(input("ID: "))
        employee = Employee.get_by_id(id)
        print(employee)


class GetPlantByIdAction(BaseAction):

    def __init__(self):
        super().__init__('Get plant by id')

    def execute(self):
        id = int(input("ID: "))
        plant = Plant.get_by_id(id)
        print(plant)


class ListAllPlantsAction(BaseAction):

    def __init__(self):
        super().__init__('List All Plants')

    def execute(self):
        for plant in Plant.get_all():
            print(f'id={plant.id} name={plant.name}')


class ListAllEmployeeAction(BaseAction):

    def __init__(self):
        super().__init__('List All Employee')

    def execute(self):
        for emp in Employee.get_all():
            print(f'id={emp.id} name={emp.name} {emp.email}')