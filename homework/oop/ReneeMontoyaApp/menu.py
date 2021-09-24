from models.plant import Plant
from models.employee import Employee


class Menu:
    def __init__(self):
        self.menu_flag = 0

    def choice(self):
        print(
            "Choose a menu item by number: \n" +
            "1. Add new Plant \n" +
            "2. Add new Employee \n" +
            "3. Get plant by id \n" +
            "4. Get employee by id \n"
        )
        self.menu_flag = int(input("Your choose: "))

    @staticmethod
    def add_new_plant():
        id = int(input("ID: "))
        location = input("Location: ")
        name = input("Name: ")
        director_id = int(input("Director ID: "))
        plant = Plant(id, location, name, director_id)
        plant.save()

    @staticmethod
    def add_new_employee():
        id = int(input("ID: "))
        name = input("Name: ")
        email = input("Email: ")
        department_type = input("Department Type: ")
        department_id = int(input("Department id: "))
        employee = Employee(id, name, email, department_type, department_id)
        employee.save()

    @staticmethod
    def get_plant_by_id():
        id = int(input("ID: "))
        plant = Plant.get_by_id(id)
        print(plant)

    @staticmethod
    def get_employee_by_id():
        id = int(input("ID: "))
        employee = Employee.get_by_id(id)
        print(employee)
