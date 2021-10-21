# Create regular class taking 8 params on init - name, last_name, phone_number, address, email, birthday, age, sex
# Override a printable string representation of Profile class and return: list of the params mentioned above

class Profile:
    def __init__(self, name, last_name, phone_number, address, email, birthday, age, sex):
        self.name = name
        self.last_name = last_name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age
        self.sex = sex
        self.list_of_the_params = [self.name, self.last_name, self.phone_number, self.address, self.email,
                                   self.birthday, self.age, self.sex]

    def __str__(self):
        return str(self.list_of_the_params)


profile = Profile("Volodymyr", "Salitrynskyi", "+38-097-251-13-53", "Zhytomyr", "volodymyr.salitrynskyi@gmail.com",
                  "06-05-1969", "52", "male")
print(profile)
