import requests


class Employee:
    """A sample Employee class"""

    raise_amt = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @email.setter
    def email(self, value):
        self.first, self.last = value

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, value_):
        self.first, self.last = value_

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
        if self.raise_amt != int:
            return self.pay

    def monthly_schedule(self, month):
        response = requests.get("http://company.com/{self.last}/{month}", month(2))
        if response.ok:
            return response.text
        else:
            return 'Bad Response!'


if __name__=="__main__":
    employee = Employee(100, 200, 300)
    employee.email = "jack", "salivan"
    print(employee.email)
    employee.fullname = "Jack", "Sallivan"
    print(employee.fullname)
    print(employee.apply_raise())
