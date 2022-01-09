class Profile:
    """
    Create regular class taking 8 params on init - name, last_name, phone_number, address, email, birthday, age, sex
    Override a printable string representation of Profile class and return: list of the params mentioned above.
    """

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
    profile = Profile("Alex", "Lys", "050-412-22-88", "IF", "my-email@mail.com", "03-22-1991", "30", "male")
    return profile


if __name__ == "__main__":
    profile1 = main()
    print(profile1)
    # ['Alex', 'Lys', '050-412-22-88', 'IF', 'my-email@mail.com', '03-22-1991', '30', 'male']
