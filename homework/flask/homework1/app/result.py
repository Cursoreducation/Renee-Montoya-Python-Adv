from calculator import Calculator


class Result(Calculator):
    def __init__(self, n1, n2):
        super(Result, self).__init__(numb1=n1, numb2=n2)

    def div_res(self):
        return f'{self.numb1} / {self.numb2} = {self.divide()}'

    def sum_res(self):
        return f'{self.numb1} + {self.numb2} = {self.add()}'

    def dif_res(self):
        return f'{self.numb1} - {self.numb2} = {self.subtract()}'

    def mult_res(self):
        return f'{self.numb1} * {self.numb2} = {self.multiply()}'

