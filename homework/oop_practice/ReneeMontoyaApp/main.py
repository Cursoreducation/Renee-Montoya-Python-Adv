from models.plant import Plant
from models.employee import Employee
from controllers.menu import Menu

if __name__ == "__main__":
    # first_plant = Plant(1, "Kyiv", "Renee", 1)
    # # first_plant = Plant(2, "Lviv", "Jack", 2)
    # first_plant.save()
    # # first_plant = Plant.get_by_id(1)
    # # print(first_plant)
    # first_employee = Employee(111, "Liubomyr Luzh", "ll@gmail.com", "plant", 1)
    # first_employee.save()
    # print(Plant.get_by_id(1))
    # print(Employee.get_by_id(1))

    menu = Menu()
    menu.menu_show()

    # enter_email = input()
    # print(Plant.get_by_email(enter_email))

    # print(f"Print DICT: {first_employee.__dict__}")
