class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def find_area(self):
        return self.width * self.height

rect_1 = Rectangle(10,50)
print(rect_1.find_area())

