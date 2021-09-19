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
        print("eating")

    @abstractmethod
    def sleep(self):
        print("sleeping")

class Lion(Animals):
    def eat(self):
        print("Lion eating")

    def sleep(self):
        print("Lion sleeping")

    def run(self):
        print("Lion runing")

    def growl(self):
        print("Lion growling")

class Rabbit(Animals):
    def eat(self):
        print("Rabbit eating")

    def sleep(self):
        print("Rabbit sleeping")

    def tremble(self):
        print("Rabbit trembling")

class Wolf(Animals):
    def eat(self):
        print("Wolf eating")

    def sleep(self):
        print("Wolf sleeping")

    def run(self):
        print("Wolf runing")

    def howl(self):
        print("Wolf howling")

class Eagle(Animals):
    def eat(self):
        print("Eagle eating")

    def sleep(self):
        print("Eagle sleeping")

    def fly(self):
        print("Eagle flying")

class Bee(Animals):
    def eat(self):
        print("Bee eating")

    def sleep(self):
        print("Bee sleeping")

    def honey(self):
        print("Bee postponing honey to honeycombs")

lion = Lion()
lion.eat()
lion.sleep()
lion.run()
lion.growl()
if isinstance(lion, Animals):
    print("Lion belongs to the Animals class")

rabbit = Rabbit()
rabbit.eat()
rabbit.sleep()
rabbit.tremble()
if isinstance(rabbit, Animals):
    print("Rabbit belongs to the Animals class")

wolf = Wolf()
wolf.eat()
wolf.sleep()
wolf.run()
wolf.howl()
if isinstance(wolf, Animals):
    print("Wolf belongs to the Animals class")

eagle = Eagle()
eagle.eat()
eagle.sleep()
eagle.fly()
if isinstance(eagle, Animals):
    print("Eagle belongs to the Animals class")

bee = Bee()
bee.eat()
bee.sleep()
bee.honey()
if isinstance(bee, Animals):
    print("Bee belongs to the Animals class")