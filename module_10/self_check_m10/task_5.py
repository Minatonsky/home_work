class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight
class Cat(Animal):
    def say(self):
        return "Meow"

# Створення екземпляра класу Cat
cat = Cat("Simon", 10)

# Виклик методу say для екземпляра класу Cat
cat_sound = cat.say()

# Вивід результату
print(f"{cat.nickname} says: {cat_sound}")
print(f"{cat.nickname}'s weight: {cat.weight}")
