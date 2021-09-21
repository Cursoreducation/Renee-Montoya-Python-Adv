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
        self.list_of_params = [self.name, self.last_name, self.phone_number, self.address, self.email, self.birthday,
                               self.age, self.sex]

    def __str__(self):
        return str(self.list_of_params)


def main():
    profile = Profile("Tom", "Rus", "0663331234", "Odessa", "rus@gmail.com", "09-22-1999", "22", "male")
    return profile


if __name__ == "__main__":
    profile1 = main()
    print(profile1)
