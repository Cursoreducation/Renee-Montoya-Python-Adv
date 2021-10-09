from .models import Model
from models.plant import Plant

class Controller():

    def __init__(self, id, location, name, menu_flag):
        self.id = id
        self.location = location
        self.name = name
        self.menu_flag = menu_flag
        self.check()

    def check(self):
        if self.menu_flag == 1:

            id_from_db = Plant.get_by_id(self.id)
            print(id_from_db)
            if id_from_db is not None:
                print("show homepage")
            else:
                print("Register")

            for item in self.generate_dict:
                if self.email is None:
                    print("Email not found. Tre again.")




