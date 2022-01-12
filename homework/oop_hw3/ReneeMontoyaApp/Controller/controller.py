from models.plant import Plant
from models.employee import Employee
# import json
import sys


class Controller:
    """When run display a menu and respond to choices"""

    plant_data = "database/plants.json"
    employee_data = "database/employees.json"

    def __init__(self):
        self.choices = {
            "1": self.new_plant,
            "2": self.new_employee,
            "3": self.get_plant_by_id,
            "4": self.get_employee_by_id,
            "quit": self.quit
        }

    @staticmethod
    def display_menu():
        print("""Choose a menu item by number:
        1. Add new Plant
        2. Add new Employee
        3. Get plant by id
        4. Get employee by id
              
        quit to exit""")

    def run(self):
        """Display menu and respond to choice"""
        while True:
            self.display_menu()
            choose = input("Your choose: ")
            event = self.choices.get(choose)
            if event:
                event()
            else:
                print(f"{choose} is not valid choice")

    # @staticmethod
    # def check_id_in_data(database, id):
    #     with open(database) as file:
    #         data = json.load(file)
    #         for dict in data:
    #             if dict['id'] == id:
    #                 return True
    #             return False

    def new_plant(self):
        try:
            id = int(input("ID: "))
        except:
            print("Only integer are valid")
            self.new_plant()
        # if self.check_id_in_data(self.plant_data, id):
        try:
            Plant.get_by_id(id)
            print(f"{id} is busy. Choose another id")
            self.new_plant()
        except:
            location = input("Location: ")
            name = input("Name: ")
            # director_id = int(input("Director ID: "))
            director_email = input("Director_email: ")
            try:
                director_id = Employee.search_email(director_email)
                plant = Plant(id, location, name, director_id)
                plant.save()
                print(f"New plant added and saved")
            except:
                print("Email not found")
                return

    def new_employee(self):
        try:
            id = int(input("ID: "))
        except:
            print("Only integer are valid")
            self.new_employee()
        # if self.check_id_in_data(self.plant_data, id):
        try:
            Plant.get_by_id(id)
            print(f"{id} is busy. Choose another id")
            self.new_employee()
        except:
            name = input("Name: ")
            email = input("Email: ")
            department_type = input("Department Type: ")
            department_id = int(input("Department id: "))
            employee = Employee(id, name, email, department_type, department_id)
            employee.save()
            print(f"New employee added and saved")

    def get_plant_by_id(self):
        try:
            id = int(input("ID: "))
        except:
            print("Only integer are valid")
            self.get_plant_by_id()
        try:
            plant = Plant.get_by_id(id)
            print(plant)
        except:
            print("There is no plant by this id")
            return

    def get_employee_by_id(self):
        try:
            id = int(input("ID: "))
        except:
            print("Only integer are valid")
            self.get_employee_by_id()
        try:
            employee = Employee.get_by_id(id)
            print(employee)
        except:
            print("There is no employee by this id")
            return

    def quit(self):
        print("Bye")
        sys.exit(0)
