class Controller:

    def __init__(self, *actions):
        self.actions = actions

    def print_menu(self):
        print('"Choose a menu item by number:')
        for index, action in enumerate(self.actions):
            print(f'{index + 1}. {action.get_action_name()}')
        print('0. Exit')

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
                except ValueError as e:
                    print('Incorrect input, please try again')
