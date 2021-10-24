# 1. Create a class hierarchy of animals with at least 5 animals that have additional methods each,
# create an instance for each of the animal and call the unique method for it.
# Determine if each of the animal is an instance of the Animals class
#

class Animals:
    """
       Parent class, should have eat, sleep
    """
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(self.name, " eats like an animal")

    def sleep(self):
        print(self.name, "sleeps like an animal")

    """
    Some of the animal with 1-2 extra methods related to this animal
    """


class Tiger(Animals):

    def hunt(self):
        print(self.name, "hunts")


class Zebra(Animals):

    def run(self):
        print(self.name, "runs")


class Lion(Animals):

    def growls(self):
        print(self.name, "says \'Aaarrrrr\'")


class Giraffe(Animals):
    def eat(self):
        print(self.name, "eats trees")


class Mammonth(Animals):
    def die_out(self):
        print(self.name, "die out")


Animal1 = Tiger("Tiger Diego")
Animal2 = Zebra("Zebra Marti")
Animal3 = Lion("Lion Alex")
Animal4 = Giraffe("Giraffe Melman")
Animal5 = Mammonth("Mammonth Manfred")

Animal1.hunt()
Animal2.run()
Animal1.eat()
Animal2.sleep()
Animal3.growls()
Animal4.eat()
Animal5.die_out()

print(isinstance(Animal1, Animals))
print(isinstance(Animal2, Animals))
print(isinstance(Animal3, Animals))
print(isinstance(Animal4, Animals))
print(isinstance(Animal5, Animals))

#
#  1.a. Create a new class Human and use multiple inheritance to create Centaur class,
#  create an instance of Centaur class and call the common method of these classes and unique.
#


class Human:
    """
    Human class, should have eat, sleep, study, work
    """
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(self.name, "eats like a human")

    def sleep(self):
        print(self.name, "sleeps like a human")

    def study(self):
        print(self.name, "studies")

    def work(self):
        print(self.name, "works")


class Centaur(Human, Animals):
    """
       Centaur class should be inherited from Human and Animal and has unique method related to it.
       """
    def ride(self):
        print(self.name, "ride a horse without horse")

    def sleep(self):
        Animals.sleep(self)


Animal6 = Centaur("Centaur Beanor")
Animal6.ride()
Animal6.eat()
Animal6.sleep()
Animal6.work()

#
# 2. Create two classes: Person, Cell Phone, one for composition, another one for aggregation.

""" 
    a.
    Make the class with composition.
    """


class Person:
    def __init__(self):
        arm_1 = Arm('Left')
        arm_2 = Arm('Right')
        self.batteries = [arm_1, arm_2]


class Arm:
    def __init__(self, side):
        self.side = side


"""
    b.
    Make the class with aggregation
    """


class CellPhone:
    def __init__(self, screen):
        self.screen = screen


class Screen:
    pass


screen1 = Screen()
phone = CellPhone(screen1)


# 3.
#     """
#     Create regular class taking 8 params on init - name, last_name, phone_number, address, email, birthday, age, sex
#     Override a printable string representation of Profile class and return: list of the params mentioned above
#     """

class Profile:
    def __init__(self, name, last_name, phone_number, address, email, birthday, age, sex):
        self.name = name
        self.last_name = last_name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age
        self.sex = sex

    def __str__(self):
        return f'name = {self.name}, last_name = {self.last_name}, phone_number = {self.phone_number}, ' \
               f'address ={self.address}, email ={self.email}, birthday={self.birthday}, age={self.age}, sex={self.sex}'


person = Profile('Solka', 'ABC', '09787', 'nizhunska 14', 'solka@mail.com', '17.07', 98, 'woman')
print(person)

#
# 4.* Create an interface for the Laptop with the next methods: Screen, Keyboard, Touchpad, WebCam, Ports, Dynamics
# and create an HPLaptop class by using your interface.

from abc import ABC, abstractmethod


class Laptop(ABC):

    @abstractmethod
    def screen(self):
        pass

    @abstractmethod
    def keyboard(self):
        pass

    @abstractmethod
    def touchpad(self):
        pass

    @abstractmethod
    def webcam(self):
        pass

    @abstractmethod
    def ports(self):
        pass

    @abstractmethod
    def dynamics(self):
        pass


class HPLaptop(Laptop):
    def __init__(self):
        self.model = {}

    def screen(self):
        self.model['screen'] = 'LCD'

    def keyboard(self):
        self.model['keyboard'] = 'logitech'

    def touchpad(self):
        self.model['touchpad'] = 'HP'

    def webcam(self):
        self.model['webcam'] = 'logitech'

    def ports(self):
        self.model['ports'] = 'usb'

    def dynamics(self):
        self.model['dynamic'] = 'HP'

    def __str__(self):
        return f'{self.model}'


HP_laptop = HPLaptop()
HP_laptop.screen()
HP_laptop.webcam()
HP_laptop.dynamics()
print(HP_laptop)
