# 2. Create two classes: Person, Cell Phone, one for composition, another one for aggregation.

class Person:
    """
    Make the class with composition.
    """

    def __init__(self):
        arm_1 = Arm('pistol')
        arm_2 = Arm('machine gun')
        self.arms = [arm_1, arm_2]

    def __str__(self):
        return f"I have the following weapons: a {self.arms[0]}, a {self.arms[1]}."

    def __del__(self):
        print('Instance of Person class was destroyed')


class Arm:
    """
    Make the class with composition.
    """

    def __init__(self, type_of_arm):
        self.type_of_arm = type_of_arm

    def __str__(self):
        return self.type_of_arm

    def __del__(self):
        print('Instance of Arm class was destroyed')


def main():
    person_ = Person()
    return person_


if __name__ == "__main__":
    person = main()
    print(person)
    # I have the following weapons: a pistol, a machine gun.
    print(person.arms)
    # [<__main__.Arm object at 0x7f89e062d040>, <__main__.Arm object at 0x7f89e062d340>]
    del person
    # Instance of Person class was destroyed
    # Instance of Arm class was destroyed
    # Instance of Arm class was destroyed
    try:
        print(person)
    except NameError:
        print("Can't print instance - it was destroy!")
        # Can't print instance - it was destroy!
    try:
        print(person.arms)
    except NameError:
        print("Can't print instance - it was destroy!")
        # Can't print instance - it was destroy!
