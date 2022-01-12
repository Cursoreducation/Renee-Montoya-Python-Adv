# 1. Create a class hierarchy of animals with at least 5 animals that have additional methods each,
# create an instance for each of the animal and call the unique method for it.
# Determine if each of the animal is an instance of the Animals class

class Animal:
    """Parent class, should have eat, sleep"""
    def eat(self):
        print('Niam')

    def sleep(self):
        print('Zzzzzz...')


class Dog(Animal):
    """Child dog class from Animals"""
    def voice(self):
        print('Gav')
    
    def walk(self):
        print('Dog walking')


class Cat(Animal):
    """Child cat class from Animals"""
    def lick(self):
        print('lick')

    def hunt(self):
        print("Cat hunting")


class Horse(Animal):
   """Child raccoon class from Animals""" 
   def run(self):
       print("Horse running")


class Parrot(Animal):
    """Child raccoon class from Animals"""
    def fly(self):
        print('Parrot flying')
    
    def repeat_words(self):
        print('Parrot repeating_words')


class Fish(Animal):
    """Child fish class from Animals"""
    def swim(self):
        print("Fish swiming")

animal1 = Dog()
animal2 = Cat()
animal3 = Horse()
animal4 = Parrot()
animal5 = Fish()

print("Dog instance: " + str(isinstance(animal1, Animal)))
print("Cat instance: " + str(isinstance(animal1, Animal)))
print("Horse instance: " + str(isinstance(animal1, Animal)))
print("Parrot instance: " + str(isinstance(animal1, Animal)))
print("Fish instance: " + str(isinstance(animal1, Animal)))

#  1.a. Create a new class Human and use multiple inheritance to create Centaur class,
#  create an instance of Centaur class and call the common method of these classes and unique.

class Human:
    def work(self):
        print("Human working")
    
    def speak(self):
        print("Human speaking")
    
    def study(self):
        print("Human studying")


class Centaur(Human, Horse):
    def imagine(self):
        print("Centaur imagine")

c = Centaur()
c.imagine()
c.work()
c.speak()
c.study()
c.run()

# 2. Create two classes: Person, CellPhone, one for composition, another one for aggregation.

class Person:
    """Class with composition"""
    def _init_(self):
        self.arm1 = Arm('left')
        self.arm2 = Arm('right')
        self.arms = [arm1, arm2]
    

class Arm:
    def __init__(self, count):
        self.count = count


class CellPhone:
    def __init__(self, model):
        self.model = model


class Screen:
    def __init__(self, quality):
        self.quality = quality


screen = Screen('Good')
iphone = CellPhone(screen)

# 3.Create regular class taking 8 params on init - name, last_name, phone_number, address, email, birthday, age, sex
# Override a printable string representation of Profile class and return: list of the params mentioned above

class Profile:
    def __init__(self, name, last_name, phone_number,\
                 adress, email, birthday, age, sex):
        self.name = name
        self.last_name = last_name
        self.phone_number = phone_number
        self.adress = adress
        self.email = email
        self.birthday = birthday
        self.age = age
        self.sex = sex

    def __repr__(self):
        return f"Profile: name = {self.name}, last_name = {self.last_name}, phone_number = {self.phone_number}, " \
              f"adress = {self.adress}, email = {self.email}, birthday = {self.birthday}, " \
              f"age = {self.age}, sex = {self.sex}"
    

p = Profile('name', 'surname', 'phone', 'adress', 'email', 'birth', '28', 'male')
print(p.__repr__)

#4.* Create an interface for the Laptop with the next methods: Screen, Keyboard, Touchpad, WebCam, Ports, Dynamics
#and create an HPLaptop class by using your interface.

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
    def __init__(self, screen_hp, keyboard_hp, touchpad_hp, webcam_hp, ports_hp, dynamics_hp):
        self.screen_hp = screen_hp
        self.keyboard_hp = keyboard_hp
        self.touchpad_hp = touchpad_hp
        self.webcam_hp = webcam_hp
        self.ports_hp = ports_hp
        self.dynamics_hp = dynamics_hp

    def screen(self):
        return f"Screen size: {self.screen_hp}\n"

    def keyboard(self):
        return f"Keyboard language: {self.keyboard_hp}\n"

    def touchpad(self):
        return f'Touchpad type: {self.touchpad_hp}\n'

    def webcam(self):
        return f'Webcam type: {self.webcam_hp}\n'

    def ports(self):
        return f'Ports type: {self.ports_hp}\n'

    def dynamics(self):
        return f'Dynamics firm: {self.dynamics_hp}\n'


hp = HPLaptop('14', 'eng', 'touchpad', 'hd webcam', 'usb 3.0', 'logitech')

print(hp.screen(), hp.keyboard(), hp.touchpad(), hp.webcam(), hp.ports(), hp.dynamics())
