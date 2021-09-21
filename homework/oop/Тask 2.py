class Person:

    def __init__(self):
        arm_1 = Arm('This is right arm')
        arm_2 = Arm('This is left arm')
        self.arms = [arm_1, arm_2]

    def __str__(self):
        return print(f" {self.arms[0]}, and {self.arms[1]}.")


class Arm:

    def __init__(self, location):
        self.location = location


person = Person()
print(person.arms)


class CellPhone:
    def __init__(self, screen):
        self.screen = screen


class Screen:
    def __init__(self):
        pass


screen = Screen()
cellphone = CellPhone(screen)

print(cellphone, screen)
del cellphone
print(screen)
