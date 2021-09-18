"""Instructions for outputting code. If you will want to see results outputs code,
you should to pick up hash sign (#) under every class."""


# 1. Task.

class Animals:

    def eat(self):
        print("Have to eat.")

    def sleep(self):
        print("Have to sleep.")


animal = Animals()


class Animal1(Animals):

    def __init__(self, type, speed):
        self.type = type
        self.speed = speed

    def __call__(self):
        return print(f"Animal 1 type: {self.type}. Speed average: {self.speed} km/h.")

    def hunt(self):
        print(f"{self.type} hunt on other animals.")


animal1 = Animal1("Lion", 80)


# animal1()
# animal1.eat()
# animal1.sleep()
# animal1.hunt()


class Animal2(Animals):

    def __init__(self, type, speed):
        self.type = type
        self.speed = speed

    def __call__(self):
        return print(f"Animal 2 type: {self.type}. Speed average: {self.speed} km/h.")

    def pet(self):
        print(f"{self.type} this is lovely pet anymore peoples.")


animal2 = Animal2("Dog", 10)


# animal2()
# animal2.eat()
# animal2.sleep()
# animal2.pet()


class Animal3(Animals):

    def __init__(self, type, speed):
        self.type = type
        self.speed = speed

    def __call__(self):
        return print(f"Animal 3 type: {self.type}. Speed average: {self.speed} km/h.")

    def fly(self):
        print(f"{self.type} be able to fly on the sky.")


animal3 = Animal3("Eagle", 120)


# animal3()
# animal3.eat()
# animal3.sleep()
# animal3.fly()


class Animal4(Animals):

    def __init__(self, type, speed):
        self.type = type
        self.speed = speed

    def __call__(self):
        return print(f"Animal 4 type: {self.type}. Speed average: {self.speed} km/h.")

    def weight(self):
        print(f"{self.type} weight about 2,500 kilograms.")


animal4 = Animal4("Elephant", 40)


# animal4()
# animal4.eat()
# animal4.sleep()
# animal4.weight()


class Animal5(Animals):

    def __init__(self, type, speed):
        self.type = type
        self.speed = speed

    def __call__(self):
        return print(f"Animal 5 type: {self.type}. Speed average: {self.speed} km/h.")

    def tall(self):
        print(f"{self.type} have tall about 6 metres.")


animal5 = Animal5("Giraffe", 4)


# animal5()
# animal5.eat()
# animal5.sleep()
# animal5.tall()

# print(isinstance(animal1, Animals))
# print(isinstance(animal2, Animals))
# print(isinstance(animal3, Animals))
# print(isinstance(animal4, Animals))
# print(isinstance(animal5, Animals))


# 1a. Task 1a.

class Human:

    def __init__(self, types, growth):
        self.types = types
        self.growth = growth

    def eat(self):
        print(f"{self.types} have to eat.")

    def sleep(self):
        print(f"{self.types} have to sleep.")

    def study(self):
        print(f"{self.types} have to study.")

    def work(self):
        print(f"{self.types} have to work.")


human = Human('People', 185)


# human.eat()
# human.sleep()
# human.study()
# human.work()


class Centaur(Animal1, Human):

    def __init__(self, type, speed, weapon, move):
        super().__init__(type, speed)
        self.weapon = weapon
        self.move = move

    def action(self):
        print(f"{self.type} can to {self.weapon} and {self.move}.")


centaur = Centaur("Centaur", 50, "archery", "run")


# centaur.hunt()
# centaur.eat()
# centaur.action()


# 2. Task 2.

class Person:
    def __init__(self):
        arm_1 = Arm('left')
        arm_2 = Arm('right')
        self.arms = [arm_1, arm_2]


class Arm:
    def __init__(self, quantity):
        self.quantity = quantity

    def __call__(self):
        return print(f"{self.quantity}")


arm = Arm(2)


# arm()
# person = Person()


class CellPhone:
    def __init__(self, model):
        self.model = model


class Screen:
    def __init__(self, size):
        self.size = size


screen = Screen('normal')
samsung = CellPhone(screen)


# 3. Task 3.

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
        return f"Name and last name:\t{self.name} {self.last_name} \nPhone_number:\t{self.phone_number} " \
               f"\nBirthday\t{self.birthday} \nAge:\t{self.age} \nSex:\t{self.sex} \nAddress:\t" \
               f"{self.address} \nEmail:\t{self.email}"


profile = Profile('Jack', 'Felix', 39231294, "19510, Jamboree Road",
                  'jf007.gmail.com', "06.19.96", 25, 'man')

# print(profile)


# 4. Task 4.

# Create an interface for the Laptop with the next methods: Screen, Keyboard, Touchpad, WebCam, Ports, Dynamics
# and create an HPLaptop class by using your interface.


from abc import ABC, abstractmethod


class Laptop(ABC):

    @abstractmethod
    def screen(self):
        raise NotImplemented

    @abstractmethod
    def keyboard(self):
        raise NotImplemented

    @abstractmethod
    def touchpad(self):
        raise NotImplemented

    @abstractmethod
    def webcam(self):
        raise NotImplemented

    @abstractmethod
    def ports(self):
        raise NotImplemented

    @abstractmethod
    def dynamics(self):
        raise NotImplemented


class HPLaptop(Laptop):

    def __init__(self, model: str):
        self.model = model

    def screen(self):
        print(f"{self.model} have 5,25 inches.")

    def keyboard(self):
        print("He have comfortable keyboard.")

    def touchpad(self):
        print(f"{self.model} have touchpad technology too.")

    def webcam(self):
        print(f"Webcam in {self.model} have 10 megapixels and filming FULL HD technology.")

    def ports(self):
        print(f"3 ports in laptop model{self.model}")

    def __call__(self):
        return self.ports

    def dynamics(self):
        print(f"Power dynamics {self.model} 40 Watt.")

# HP = HPLaptop('HP')
# HP.screen()
# HP.keyboard()
# HP.touchpad()
# HP.dynamics()
# HP()
# HP.webcam()
