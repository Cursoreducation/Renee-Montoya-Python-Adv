from animals import Animals


class Human:
    """
    Human class, should have eat, sleep, study, work
    """

    def __init__(self, name) -> None:
        super().__init__()
        self.name = name

    def eat(self):
        print(self.name + ': I am eat')

    def sleep(self):
        print(self.name + ': I am sleep')

    def study(self):
        print(self.name + ': I am study')

    def work(self):
        print(self.name + ': I am work')


class Centaur(Human, Animals):
    """
    Centaur class should be inherited from Human and Animal and has unique method related to it.
    """

    def gallop(self):
        print(self.name + ': I am gallop')

    def jump(self):
        print(self.name + ': I am jump')


if __name__ == '__main__':
    human = Human('Ivan')
    human.eat()
    human.work()
    human.sleep()
    centaur = Centaur('Haron')
    centaur.eat()
    centaur.work()
    centaur.jump()
    centaur.gallop()
