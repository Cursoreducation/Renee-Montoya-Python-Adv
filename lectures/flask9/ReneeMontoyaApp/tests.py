class A:
    address = "Naukova"

    def __init__(self, name):
        self.name = name

    def get_name(self):
        print(self.name)

    @classmethod
    def hello_static(cls):
        print(cls.address)


A.hello_static()

