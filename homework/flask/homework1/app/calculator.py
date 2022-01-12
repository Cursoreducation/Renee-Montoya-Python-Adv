class Calculator:

    def __init__(self, numb1, numb2):
        self.numb1 = numb1
        self.numb2 = numb2

    def add(self):
        return self.numb1 + self.numb2

    def subtract(self):
        return self.numb1 - self.numb2

    def multiply(self):
        return self.numb1 * self.numb2

    def divide(self):
        if self.numb2 == 0:
            raise ValueError('Can not divide by zero!')

        return self.numb1 / self.numb2
