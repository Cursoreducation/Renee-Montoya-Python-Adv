from controller import Controller
from actions import AddNewEmployeeAction, AddNewPlantAction, GetEmployeeByIdAction, GetPlantByIdAction

if __name__ == '__main__':
    controller = Controller(AddNewPlantAction(), AddNewEmployeeAction(), GetPlantByIdAction(), GetEmployeeByIdAction())
    controller.run()