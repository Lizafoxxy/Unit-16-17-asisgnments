class Client:
    def __init__(self, name, surname, city, balance):
        self.name = name
        self.surname = surname
        self.city = city
        self.balance = balance

    def __str__(self):
        return f'''"{self.name} {self.surname}. {self.city}. Баланс: {self.balance} руб."'''

    def get_pers_info(self):
        return(f"Имя: {self.name}\nФамилия: {self.surname}\nГород: {self.city}\n")


user_1 = Client("Иван", "Петров", "Москва", 50)
user_2 = Client("Семен", "Сидоров", "Ижевск", 25)
user_3 = Client("Петр", "Иванов", "Омск", 33)

invite_list = [user_1, user_2, user_3]

for user in invite_list:
    print(user.get_pers_info())


