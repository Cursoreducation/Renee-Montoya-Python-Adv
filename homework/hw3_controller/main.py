from actions import AddNewEmployeeAction, AddNewPlantAction, GetEmployeeByIdAction, GetPlantByIdAction, \
    ListAllPlantsAction, ListAllEmployeeAction
from controller import Controller

if __name__ == '__main__':
    controller = Controller(
        AddNewPlantAction(),
        AddNewEmployeeAction(),
        GetPlantByIdAction(),
        GetEmployeeByIdAction(),
        ListAllPlantsAction(),
        ListAllEmployeeAction(),
    )
    controller.run()
