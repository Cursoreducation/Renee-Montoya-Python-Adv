class Animals:

    def eat(self):
        print("I eat.")

    def sleep(self):
        print("I must to sleep.")

    def drink_water(self):
        print("Also i drink water.")


class Dog(Animals):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.type = "dog"

    def speak(self):
        print("I am", self.name, "and I am", self.age, "years old")

    def run(self):
        print("I run very fast.")


dog = Dog("Tim", 5)
dog.speak()
dog.eat()
dog.sleep()
dog.drink_water()
dog.run()


class Cat(Animals):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.type = "cat"

    def meow(self):
        print(self.name, "Meow.")


cat = Cat("Myrsik", 2)

cat.eat()
cat.sleep()
cat.drink_water()
cat.meow()


class Bird(Animals):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.type = "bird"

    def fly(self):
        print(self.name, "can fly.")

    def catch_fish(self):
        print("I can catch a big fish.")


bird = Bird("Bill", 1)

bird.eat()
bird.sleep()
bird.drink_water()
bird.fly()
bird.catch_fish()


class Dolphin(Animals):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.type = "dolphin"

    def swim(self):
        print(self.name, "can swim.")

    def play(self):
        print("I can play with you.")


dolphin = Dolphin("Pol", 3)

dolphin.eat()
dolphin.sleep()
dolphin.swim()
dolphin.play()


class Cow(Animals):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.type = "cow"

    def produce(self):
        print(self.name, "produce milk.")

    def walk(self):
        print("I can walk.")


cow = Cow("Kazka", 6)

cow.eat()
cow.sleep()
cow.produce()
cow.walk()

print(isinstance(dog, Animals))
print(isinstance(cat, Animals))
print(isinstance(bird, Animals))
print(isinstance(dolphin, Animals))
print(isinstance(cow, Animals))


class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name} can eat.")

    def sleep(self):
        print(f"In {self.age} years old you must sleep 8 hours.")

    def study(self):
        print("Can study")

    def work(self):
        print("Can work")

    def self_improvement(self):
        print("Can self_improvement")


human = Human("Jon", 26)
human.eat()
human.sleep()
human.study()
human.work()
human.self_improvement()


class Centaur(Animals, Human):
    def __init__(self, name, age, move):
        super().__init__(name, age)
        self.name = name
        self.move = move
        self.age = age

    def say(self):
        print(f"Hello,I`m {self.name}.I can {self.move}")


centaur = Centaur("Centaur", 70, "run")
centaur.drink_water()
centaur.work()
centaur.say()
