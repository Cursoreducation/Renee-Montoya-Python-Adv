class Profile:

    def __init__(self, name, last_name, phone_number, address, email, birthday, age, sex) -> None:
        super().__init__()
        self.name = name
        self.last_name = last_name
        self.phone = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age
        self.sex = sex

    def __str__(self) -> str:
        return f'{self.name} {self.last_name} {self.phone} {self.address} {self.email} {self.birthday} {self.age} {self.sex}'


if __name__ == "__main__":
    profile = Profile('Ivan', 'Ivanov', '3432', 'Kiev', 'www@ww.ww', '12.12.12', 12, True)
    print(profile)
