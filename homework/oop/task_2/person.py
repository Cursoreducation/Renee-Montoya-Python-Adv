class Arm:
    pass


class Person:
    def __init__(self) -> None:
        super().__init__()
        self.arms = (Arm(), Arm())

    def get_right_arm(self):
        return self.arms[0]

    def get_left_arm(self):
        return self.arms[1]
