class Animals:
    """
    Parent class, should have eat, sleep
    """

    def eat(self):
        print(self.__class__.__name__ + ': I am eat')

    def sleep(self):
        print(self.__class__.__name__ + ': I am sleep')


class Bird(Animals):

    def fly(self):
        print(self.__class__.__name__ + ': I am fly')


class Dragon(Animals):

    def fly(self):
        print(self.__class__.__name__ + ': I am fly')

    def swim(self):
        print(self.__class__.__name__ + ': I am swim')


class Fish(Animals):

    def swim(self):
        print(self.__class__.__name__ + ': I am swim')


class Wolf(Animals):

    def run(self):
        print(self.__class__.__name__ + ': I am run')


class Lion(Animals):

    def run(self):
        print(self.__class__.__name__ + ': I am run')


if __name__ == '__main__':
    lion = Lion()
    print(isinstance(lion, Animals))
    lion.run()
    wolf = Wolf()
    print(isinstance(wolf, Animals))
    wolf.run()
    bird = Bird()
    print(isinstance(bird, Animals))
    bird.fly()
    fish = Fish()
    print(isinstance(fish, Animals))
    fish.swim()
    dragon = Dragon()
    print(isinstance(dragon, Animals))
    dragon.fly()
    dragon.swim()
