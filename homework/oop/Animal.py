# 1. Create a class hierarchy of animals with at least 5 animals that have additional methods each,
# create an instance for each of the animal and call the unique method for it.
# Determine if each of the animal is an instance of the Animals class


class Animals:
    """
    Parent class, should have eat, sleep
    """

    @staticmethod
    def eat():
        return "I can eat!"

    @staticmethod
    def sleep():
        return "I can sleep!"

    @staticmethod
    def tail():
        return "I have a tail!"


class Lion(Animals):
    """
    Some of the animal with 1-2 extra methods related to this animal
    """

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    @staticmethod
    def run():
        return "I'm fast!"

    @staticmethod
    def hunt():
        return "I'm hunting!"

    def actions(self):
        print(self.run())
        print(self.hunt())


class Mouse(Animals):

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    @staticmethod
    def search():
        return "I'm looking for grain!"

    @staticmethod
    def say():
        return "Pi-pi"

    def actions(self):
        print(self.search())
        print(self.say())


class Bear(Animals):

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    @staticmethod
    def swim():
        return "I'm fishing!"

    @staticmethod
    def say():
        return "Brrr"

    def actions(self):
        print(self.swim())
        print(self.say())


class Giraffe(Animals):

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    @staticmethod
    def grow():
        return "I'm high!"

    @staticmethod
    def drink():
        return "I'm like drink water!"

    def actions(self):
        print(self.grow())
        print(self.drink())


class Pigeon(Animals):

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    @staticmethod
    def fly():
        return "I'm flying!"

    @staticmethod
    def incubate():
        return "I incubate eggs!"

    def actions(self):
        print(self.fly())
        print(self.incubate())


def main():
    animals = []
    leo1 = Lion("Leo")
    animals.append(leo1)
    mouse1 = Mouse("Mickey")
    animals.append(mouse1)
    bear1 = Bear("Tom")
    animals.append(bear1)
    giraffe1 = Giraffe("Frank")
    animals.append(giraffe1)
    pigeon1 = Pigeon("Ikar")
    animals.append(pigeon1)

    for i in range(0, len(animals)):
        print(f"I'm a {type(animals[i]).__name__}. My name is {animals[i]}.")
        print(animals[i].eat())
        print(animals[i].sleep())
        animals[i].actions()

        if isinstance(animals[i], Animals):
            print("I belong to the Animal class.")

        print("*" * 35)


if __name__ == "__main__":
    main()
