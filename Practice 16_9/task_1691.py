class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    # создаем метод repr для того, чтобы нужная форма возращалась нам при просто запросе переменной в консоли
    # только непонятно каку вызывать эту переменную в консоли - не срабатывает, выдает ошибку name r_1 is not defined.
    # def __repr__(self):
    #     return f"Rectangle : {self.x}, {self.y}, {self.width}, {self.height}."

    def __str__(self):
        return f"Rectangle : {self.x}, {self.y}, {self.width}, {self.height}."


r_1 = Rectangle(5, 10, 50, 100)

print(r_1)