import sys
from models.plant import Plant
from models.employee import Employee
import json


class Menu:
    def __init__(self):
        self.choices = {
                "1": self.add_plant,
                "2": self.add_employee,
                "3": self.get_plant_by_id,
                "4": self.get_employee_by_id,
                "5": self.quit
                }

    @staticmethod
    def display_menu():
        print("Choose a menu item by number: \n" +
              "1. Add new Plant \n" +
              "2. Add new Employee \n" +
              "3. Get plant by id \n" +
              "4. Get employee by id \n" +
              "5. Exit \n")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Your choose: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))

    @staticmethod
    def get_id_by_email(input_email):
        with open('database/employees.json', 'r') as user_file:
            user_data = json.loads(user_file.readline())
            for email in user_data:
                if input_email == email['email']:
                    director_id = email['id']
                    return director_id
            return False

    @staticmethod
    def add_plant():
        id = int(input("ID: "))
        location = input("Location: ")
        name = input("Name: ")
        print("Choose an option: \n" +
              "1. Input director ID \n" +
              "2. Input email employee \n")
        menu_flag = int(input("Your choose: "))
        if menu_flag == 1:
            director_id = int(input("Director ID: "))
        elif menu_flag == 2:
            email = input("Email: ")
            get_id = Menu.get_id_by_email(email)
            if get_id:
                director_id = get_id
            else:
                print("Emloyee with this email doesn't exists. \n")
                return 0
        else:
            print("{0} is not a valid choice".format(menu_flag))
        plant = Plant(id, location, name, director_id)
        plant.save()

    @staticmethod
    def add_employee():
        id = int(input("ID: "))
        name = input("Name: ")
        email = input("Email: ")
        department_type = input("Department Type: ")
        department_id = input("Department ID: ")
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

    @staticmethod
    def quit():
        sys.exit(0)
