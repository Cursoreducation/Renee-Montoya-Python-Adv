from menu import Menu

if __name__ == '__main__':
    menu = Menu()

    while True:
        menu.choice()
        if menu.menu_flag == 1:
            menu.add_new_plant()
        elif menu.menu_flag == 2:
            menu.add_new_employee()
        elif menu.menu_flag == 3:
            menu.get_plant_by_id()
        elif menu.menu_flag == 4:
            menu.get_employee_by_id()
        else:
            break
