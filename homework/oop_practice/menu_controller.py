from models.plant import Plant
from models.employee import Employee


class EmailError(Exception):
    pass


class MenuController:

    def __init__(self, action=None):
        self.action = action

    def choice_menu(self):
        self.action = int(input("Choose a menu item by number: \n" +
                                "1. Add new Plant \n" +
                                "2. Add new Employee \n" +
                                "3. Get plant by id \n" +
                                "4. Get employee by id \n "
                                "\n: "))
        try:
            if self.action == 1:
                self.add_new_plant()
            if self.action == 2:
                self.add_new_employee()
            if self.action == 3:
                self.get_plant_by_id()
            if self.action == 4:
                self.get_employee_by_id()
        except ValueError:
            print("Input type integer for this action!")

    def add_new_plant(self):
        try:
            id = int(input("ID: "))
        except ValueError:
            print("Input only number here.")
            return
        location = input("Location: ")
        name = input("Name: ")
        email = input("Director_email: ")
        try:
            employee_ = Employee.find_email(email)
        except EmailError:
            print("The email haven't")
            return
        try:
            plant = Plant(id, location, name, employee_.id)
            plant.save()
        except AttributeError:
            print("Attribute error. Run the process anew.")

    def add_new_employee(self):
        id = int(input("ID: "))
        name = input("Name: ")
        email = input("Email: ")
        department_type = input("Department Type: ")
        department_id = int(input("Department id: "))
        employee = Employee(id, name, email, department_type, department_id)
        employee.save()

    def get_plant_by_id(self):
        id = int(input("ID: "))
        plant = Plant.get_by_id(id)
        print(plant)

    def get_employee_by_id(self):
        id = int(input("ID: "))
        employee = Employee.get_by_id(id)
        print(employee)
