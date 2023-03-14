class Client:
    def __init__(self, name, surname, city, balance):
        self.name = name
        self.surname = surname
        self.city = city
        self.balance = balance

    def __str__(self):
        return f'''"{self.name} {self.surname}. {self.city}. Баланс: {self.balance} руб."'''

user_1 = Client("Иван", "Петров", "Москва", 50)

print(user_1)

