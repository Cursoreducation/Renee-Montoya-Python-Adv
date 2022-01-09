from controllers import check_data
from models.plant import Plant
from models.employee import Employee


class Menu:

    def menu_show(self):
        while True:
            print("*" * 35 + "\n" +
                  "Choose the menu item by number: \n" +
                  "1. Add new Plant \n" +
                  "2. Add new Employee \n" +
                  "3. Get plant by ID \n" +
                  "4. Get employee by ID \n" +
                  "5. Get director ID by email \n" +
                  "6. Exit \n" +
                  "*" * 35 + "\n")
            try:
                menu_flag = int(input("Your choose: "))
            except ValueError:
                print("Enter correct number.")
                continue
            if menu_flag == 1:
                self.add_plant()
            elif menu_flag == 2:
                self.add_employee()
            elif menu_flag == 3:
                self.get_plant_by_id()
            elif menu_flag == 4:
                self.get_employee_by_id()
            elif menu_flag == 5:
                self.get_employee_id_by_email()
            elif menu_flag == 6:
                break
            else:
                print("Enter correct number.")

    @staticmethod
    def add_plant():
        flag = True
        while flag:
            id_plant = int(input("ID: "))
            if not check_data.check_data_is_present(Plant, 'id', id_plant):
                flag = False
            else:
                print("This ID is already present!")

        location = input("Location: ")

        name = input("Name: ")

        director_id = int(input("Director ID: "))
        while check_data.check_data_is_present(Employee, 'id', director_id):
            continue
        else:
            print("No employee with this ID was found! Want to use this ID?\nYes - 1 / No - 2")
            flag_answer = True
            while flag_answer:
                try:
                    answer = int(input())
                    if answer == 1:
                        director_id = director_id
                        flag_answer = False
                    elif answer == 2:
                        director_id = int(input("Enter NEW Director ID: "))
                except ValueError:
                    print("Enter correct answer.")

        plant = Plant(id_plant, location, name, director_id)
        plant.save()

    @staticmethod
    def add_employee():
        id = int(input("ID: "))
        name = input("Name: ")
        email = input("Email: ")
        department_type = input("Department Type: ")
        department_id = int(input("Department ID: "))
        employee = Employee(id, name, email, department_type, department_id)
        employee.save()

    @staticmethod
    def get_plant_by_id():
        id = int(input("ID: "))
        plant = Plant.get_by_id(id)
        return plant

    @staticmethod
    def get_employee_by_id():
        id = int(input("ID: "))
        employee = Employee.get_by_id(id)
        print(employee)

    @staticmethod
    def get_employee_id_by_email():
        email = input("Enter email: ")
        director_id = Plant.get_by_email(email)
        print(f"Director ID with email <{email}>: {director_id}")
        # print(director_id)
