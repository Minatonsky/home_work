class Animal:
    color = "white"

    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight
    @classmethod
    def change_color(self,color):
        self.color = color

first_animal = Animal("Simon", 10)
second_animal = Animal("Liza", 15)
Animal.change_color("red")
print(first_animal.color)
print(second_animal.color)