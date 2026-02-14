'''
Завдання 1 -

Попрацюйте над складним класом, що породжений кількома класами.
У кожного з класів, від яких успадковується результівний,
мають бути ексклюзивні атрибути та методи, які доступні в дочірньому.

'''


class Breed:
    def __init__(self, breed):
        self.breed = breed

class Size:
    def __init__(self, size):
        self.size = size

class Age:
    def __init__(self, age):
        self.age = age

class Dog(Breed, Size, Age):
    def __init__(self, breed, size, age):
        Breed.__init__(self, breed)
        Size.__init__(self, size)
        Age.__init__(self, age)


