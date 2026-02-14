'''
Завдання 1 -

Попрацюйте над складним класом, що породжений кількома класами.
У кожного з класів, від яких успадковується результівний,
мають бути ексклюзивні атрибути та методи, які доступні в дочірньому.

'''

class Shape:
    def shape_type(self):
        return "Geometric shape"

class Color:
    def set_color(self, color):
        self.color = color

class Size:
    def set_size(self, size):
        self.size = size

class Rectangle(Shape, Color, Size):
    def __init__(self, color, size):
        self.set_color(color)
        self.set_size(size)

    def area(self, width, height):
        return width * height

rectangle = Rectangle("Yellow", 20)

print(rectangle.shape_type())
print(rectangle.color)
print(rectangle.size)
print(rectangle.area(5, 10))





