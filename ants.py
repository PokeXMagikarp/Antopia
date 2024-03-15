
class Ant:
    def __init__(self, position, health, speed, color):
        self.health = health
        self.speed = speed
        self.color = color
        self.position=position

    def move(self):
        print(f"The ant is moving at {self.speed} speed.")

    def attack(self):
        print(f"The ant is attacking with {self.health} health.")

    def eat(self):
        print(f"The ant is eating with {self.color} color.")

class PoisonAnt(Ant):
    def __init__(self,position, health, speed, color, poison_damage):
        super().__init__(health, speed, color, position)
        self.poison_damage = poison_damage

    def poison_attack(self):
        print(f"The poison ant is attacking with {self.health} health and inflicting {self.poison_damage} poison damage.")

    def eat(self):
        print(f"The poison ant is eating with {self.color} color and absorbing toxins.")