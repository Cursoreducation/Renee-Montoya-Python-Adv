# 1.a. Create a new class Human and use multiple inheritance to create Centaur class, create an
# instance of Centaur class and call the common method of these classes and unique.

from Animal import Animals


class Human:
    """
    Human class, should have eat, sleep, study, work
    """

    def __init__(self, name):
        self.name = name

    @staticmethod
    def eat():
        return "I'm eating"

    @staticmethod
    def sleep():
        return "I'm sleeping"

    @staticmethod
    def study():
        return "I'm studying"

    @staticmethod
    def work():
        return "I'm working"

    def __str__(self):
        return self.name

    def actions(self):
        print(self.eat())
        print(self.sleep())
        print(self.study())
        print(self.work())


class Centaur(Human, Animals):
    """
    Centaur class should be inherited from Human and Animal and has unique method related to it.
    """

    def __init__(self, name):
        super().__init__(name)
        self.name = name

    @staticmethod
    def say():
        return "I have 4 legs!"

    def __str__(self):
        return self.name

    def actions(self):
        print(super(Centaur, self).eat(), "<-- From Human class")
        print(super(Centaur, self).sleep(), "<-- From Human class")
        print(super(Centaur, self).work(), "<-- From Human class")
        print(super(Centaur, self).study(), "<-- From Human class")
        print(self.tail(), "<-- From Animal class")
        print(self.say(), "<-- Unique method")


def main():
    human1 = Human("Hercules")
    print(f"I'm a {type(human1).__name__}. My name is {human1}.")
    # I'm a Human. My name is Hercules.
    human1.actions()
    # I'm eating
    # I'm sleeping
    # I'm studying
    # I'm working
    print("*" * 35)

    def create_centaur(**kwargs):
        centaur = Centaur(kwargs['name'])
        print(f"I'm a {type(centaur).__name__}. My name is {centaur}.")
        # I'm a Centaur. My name is Titeron.
        return centaur

    centaur1 = create_centaur(name="Titeron")
    print("I belong to the Centaur class. -->", isinstance(centaur1, Centaur))
    # I belong to the Centaur class. --> True
    centaur1.actions()
    # I'm eating <-- From Human class
    # I'm sleeping <-- From Human class
    # I'm working <-- From Human class
    # I'm studying <-- From Human class
    # I have a tail! <-- From Animal class
    # I have 4 legs! <-- Unique method


if __name__ == "__main__":
    main()
