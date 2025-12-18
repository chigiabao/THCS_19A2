from abc import ABC, abstractmethod
class Character(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def attack(self):
        pass

class Warrior(Character):
    def attack(self):
        print(f"{self.name} vung kiếm chém mạnh! (Sát thương vật lý)")

class Mage(Character):
    def attack(self):
        print(f"{self.name} niệm chú bắn cầu lửa! (Sát thương phép)")
team = [Warrior("Arthur"), Mage("Merlin")]
for char in team:
    char.attack()