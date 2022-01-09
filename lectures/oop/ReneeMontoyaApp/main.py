from abc import ABC, abstractmethod

from models.plant import Plant
from models.employee import Employee


class Main(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def execute(self):
        pass

    def get_action_name(self):
        return self.name


class AddNewPlant(Main):
    def __init__(self):
        super().__init__('Add new Plant')

    def execute(self):
        id = int(input("ID: "))
        location = input("Location: ")
        name = input("Name: ")
        director_id = int(input("Director ID: "))
        plant = Plant(id, location, name, director_id)
        email = input('Director E-Mail: ')
        try:
            empl = Employee.search_by_email(email)
        except Exception as _:
            print('Email not Found')
            return
        plant = Plant(id, location, name, empl.id)
        plant.save()


class AddNewEmployee(Main):

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


class GetPlantById(Main):

    def __init__(self):
        super().__init__('Get plant by id')

    def execute(self):
        id = int(input("ID: "))
        plant = Plant.get_by_id(id)
        print(plant)


class GetEmployeeById(Main):

    def __init__(self):
        super().__init__('Get employee by id')

    def execute(self):
        id = int(input("ID: "))
        employee = Employee.get_by_id(id)
        print(employee)


class Controller:
    def __init__(self, *actions):
        self.actions = actions

    def print_menu(self):
        print('Choose a menu item by number:\n'
              "1. Add new Plant \n" +
              "2. Add new Employee \n" +
              "3. Get plant by id \n" +
              "4. Get employee by id \n"
              "0. Exit")

    def run(self):
        if self.actions:
            while True:
                self.print_menu()
                try:
                    select_value = int(input("Your choose: ")) - 1
                    if len(self.actions) > select_value >= 0:
                        self.actions[select_value].execute()
                    elif select_value == -1:
                        break

                except ValueError:
                    print("Incorrect input")


if __name__ == '__main__':
    controller = Controller(AddNewPlant(), AddNewEmployee(), GetPlantById(),
                            GetEmployeeById())
    controller.run()
