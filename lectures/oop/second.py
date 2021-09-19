from abc import ABC, abstractmethod


class Car(ABC):
    def peredacha(self):
        print('1')

    @abstractmethod
    def bibi(self):
        print("Bi Bi")


class Toyota:
    def move(self):
        print("Toyota move")

    def znak(self):
        print("Toyota")


class ToyotaCamry(Car, Toyota):
    def __init__(self, owner_name, engine):
        self.owner_name = owner_name
        self.engine = engine

    def move(self):
        super(ToyotaCamry, self).move()
        print("Dzelenchit motors")

    @staticmethod
    def exampleStatic():
        print("Example Static Static")


    def bibi(self):
        print("Bi Bi from Toyota")

    def __str__(self):
        return self.owner_name

    def __len__(self):
        return 3

    def __call__(self, *args, **kwargs):
        print(kwargs['engine'])
        print(args[0] - args[1])

    def get_owner_info(self):
        print(self.owner_name)

    def get_car_info(self):
        self.znak()
        self.get_owner_info()
        print(self.engine)

    def __del__(self):
        print("Na metalolom")


ToyotaCamry.exampleStatic()

# car = ToyotaCamry("Vasyl", "3.5")
# car.get_owner_info()
# car2 = ToyotaCamry("Petro", "2.0")
# car2.get_owner_info()
