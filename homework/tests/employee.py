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

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def monthly_schedule(self, month):
        response = requests.get("http://company.com/{self.last}/{month}")
        if response.ok:
            return response.text
        else:
            return 'Bad Response!'

#
# if __name__ == '__main__':
#     user = Employee("kkk", "kkk", 8990)
#     print(user.pay)
#     user.apply_raise()
#     print(user.pay)
#     print(user.monthly_schedule('lune'))
