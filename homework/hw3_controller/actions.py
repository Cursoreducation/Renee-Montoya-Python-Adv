from abc import ABC, abstractmethod

from models.plant import Plant
from models.employee import Employee

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
        id = int(input("ID: "))
        location = input("Location: ")
        name = input("Name: ")
        director_id = int(input("Director ID: "))
        plant = Plant(id, location, name, director_id)
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

