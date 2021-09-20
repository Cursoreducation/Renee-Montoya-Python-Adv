from abc import abstractmethod
from animals import Animals


class Human:
    """
    Human class, should have eat, sleep, study, work
    """

    @abstractmethod
    def study(self):
        print("study")

    @abstractmethod
    def work(self):
        print("work")


class Centaur(Animals, Human):
    """
    Centaur class should be inherited from Human and Animal and has unique method related to it.
    """

    def __init__(self, owner_name):
        self.owner_name = owner_name

    def eat(self):
        print("Centaur " + self.owner_name + " eating")

    def sleep(self):
        print("Centaur " + self.owner_name + " sleeping")

    def study(self):
        print("Centaur " + self.owner_name + " studying")

    def work(self):
        print("Centaur " + self.owner_name + " working")

    def run(self):
        print("Centaur " + self.owner_name + " runing")


centaur = Centaur("Horse")
centaur.eat()
centaur.sleep()
centaur.study()
centaur.work()
centaur.run()
if isinstance(centaur, Animals):
    print("Centaur belongs to the Animals class")
if isinstance(centaur, Human):
    print("Centaur belongs to the Human class")
