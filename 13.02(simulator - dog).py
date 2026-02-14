'''
Звдання 2 -
Попрацюйте над власною симуляцією, що має складатися мінімум із двох класів, пов'язаних між собою.

Класи - Dog, Breed, Carer
'''

import random

class Dog:
    def __init__(self, name="", breed=None, carer=None):
        self.name = name
        self.gladness = 50
        self.satiety = 50
        self.breed = breed
        self.carer = carer

    def get_breed(self):
        self.breed = Breed(breed_list)

    def get_carer(self):
        self.carer = Carer(carer_list)

    def play(self):
        self.gladness += 10
        self.satiety -= 5
        print(f"{self.name} played")

    def eat(self):
        self.satiety += 15
        self.gladness += 2
        print(f"{self.name} ate some food")

    def sleep(self):
        self.gladness += 5
        self.satiety -= 3
        print(f"{self.name} slept")

    def random_action(self):
        action = random.choice(["play", "eat", "sleep"])
        if action == "play":
            self.play()
        elif action == "eat":
            self.eat()
        else:
            self.sleep()

    def days_indexes(self, day):
        day_str = f" Today the {day} of {self.name}'s life "
        print(f"{day_str:=^50}\n")
        print(f"Satiety – {self.satiety}")
        print(f"Gladness – {self.gladness}\n")

    def is_alive(self):
        if self.gladness <= 0:
            print(f"{self.name} is depressed")
            return False
        if self.satiety <= 0:
            print(f"{self.name} is dead")
            return False
        return True

    def live(self, day):
        if not self.is_alive():
            return False

        if self.breed is None:
            self.get_breed()
            print(f"Joy is a {self.breed.name}")

        if self.carer is None:
            self.get_carer()
            print(f"Jame got a carer named {self.carer.name}")

        self.random_action()

        self.days_indexes(day)


class Breed:
    def __init__(self, breed_list):
        self.name = random.choice(breed_list)


class Carer:
    def __init__(self, carer_list):
        self.name = random.choice(carer_list)


breed_list = [
    "Italian Greyhound",
    "Whippet",
    "Border Collie",
    "Miniature Pinscher",
    "English Setter"
]

carer_list = [
    "Orin",
    "Henry",
    "Azura",
    "Nyx",
    "Nora"
]

dog_name = input("Enter dog's name: ")
nick = Dog(name=dog_name)
for day in range(1, 8):
    if nick.live(day) == False:
        break

