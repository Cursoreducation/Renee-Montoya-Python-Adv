class ToyotaCamry:
    engine = "3.5 diesel"

    def __init__(self, owner_name):
        self.owner_name = owner_name

    def get_owner_info(self):
        print(self.owner_name)

    def get_car_info(self):
        print(self.engine)

    def move(self):
        print('move')


car = ToyotaCamry("Vasyl")
car.move()
car.get_owner_info()
car.get_car_info()

car2 = ToyotaCamry("Petro")
car2.get_owner_info()