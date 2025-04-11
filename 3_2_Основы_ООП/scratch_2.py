class Weapon:
    def __init__(self, damage):
        self.damage = damage
        print(f"Создано оружие с уроном {self.damage}")

class Sword(Weapon):
    def __init__(self, damage, length):
        super().__init__(damage)
        self.length = length
        print(f"Меч длиной {self.length} cm c уроном {self.damage} dmg")

katana = Sword(50, 100)