# 2. Create two classes: Person, Cell Phone, one for composition, another one for aggregation.

class Person:
    """
    Class with composition.
    """

    def __init__(self):
        arm1 = Arm("Knife")
        arm2 = Arm("Gun")
        self.arms = [arm1, arm2]

    def __str__(self):
        return f"I have weapons: {self.arms[0]} and {self.arms[1]}"


class Arm:
    """
    Class with composition.
    """

    def __init__(self, arm):
        self.arm = arm

    def __str__(self):
        return self.arm


class CellPhone:
    """
    Class with aggregation
    """

    def __init__(self, screen_phone):
        self.screen = screen_phone


class Screen:
    """
    Class with aggregation
    """
    def __init__(self):
        pass


person = Person()
print("Instance of Person:", person)
print("Instances of Arm:", person.arms[0], "and", person.arms[1])

screen = Screen()
cell_phone = CellPhone(screen)
print(cell_phone)
print(cell_phone.screen)
print(screen)
