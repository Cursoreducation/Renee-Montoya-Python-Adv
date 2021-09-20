# 1. Create a class hierarchy of animals with at least 5 animals that have additional methods each,
# create an instance for each of the animal and call the unique method for it.
# Determine if each of the animal is an instance of the Animals class

from abc import abstractmethod


class Animals:
    """
    Parent class, should have eat, sleep
    """

    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def sleep(self):
        pass


class Lion(Animals):
    def __init__(self, owner_name):
        self.owner_name = owner_name

    def eat(self):
        print("Lion " + self.owner_name + " eating")

    def sleep(self):
        print("Lion " + self.owner_name + " sleeping")

    def run(self):
        print("Lion " + self.owner_name + " running")

    def growl(self):
        print("Lion " + self.owner_name + " growling")


class Rabbit(Animals):
    def __init__(self, owner_name):
        self.owner_name = owner_name

    def eat(self):
        print("Rabbit " + self.owner_name + " eating")

    def sleep(self):
        print("Rabbit " + self.owner_name + " sleeping")

    def tremble(self):
        print("Rabbit " + self.owner_name + " trembling")


class Wolf(Animals):
    def __init__(self, owner_name):
        self.owner_name = owner_name

    def eat(self):
        print("Wolf " + self.owner_name + " eating")

    def sleep(self):
        print("Wolf " + self.owner_name + " sleeping")

    def run(self):
        print("Wolf " + self.owner_name + " running")

    def howl(self):
        print("Wolf " + self.owner_name + " howling")


class Eagle(Animals):
    def __init__(self, owner_name):
        self.owner_name = owner_name

    def eat(self):
        print("Eagle " + self.owner_name + " eating")

    def sleep(self):
        print("Eagle " + self.owner_name + " sleeping")

    def fly(self):
        print("Eagle " + self.owner_name + " flying")


class Bee(Animals):
    def __init__(self, owner_name):
        self.owner_name = owner_name

    def eat(self):
        print("Bee " + self.owner_name + " eating")

    def sleep(self):
        print("Bee " + self.owner_name + " sleeping")

    def honey(self):
        print("Bee " + self.owner_name + " postponing honey to honeycombs")


lion = Lion("Simba")
lion.eat()
lion.sleep()
lion.run()
lion.growl()
if isinstance(lion, Animals):
    print("Lion belongs to the Animals class")

rabbit = Rabbit("Roger")
rabbit.eat()
rabbit.sleep()
rabbit.tremble()
if isinstance(rabbit, Animals):
    print("Rabbit belongs to the Animals class")

wolf = Wolf("Grey")
wolf.eat()
wolf.sleep()
wolf.run()
wolf.howl()
if isinstance(wolf, Animals):
    print("Wolf belongs to the Animals class")

eagle = Eagle("Aquila")
eagle.eat()
eagle.sleep()
eagle.fly()
if isinstance(eagle, Animals):
    print("Eagle belongs to the Animals class")

bee = Bee("Maya")
bee.eat()
bee.sleep()
bee.honey()
if isinstance(bee, Animals):
    print("Bee belongs to the Animals class")
