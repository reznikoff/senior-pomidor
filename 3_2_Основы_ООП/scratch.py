class Character:
    def __init__(self, name, race, level, base_damage):
        self.name = name
        self.race = race
        self.level = level
        self.health = 100
        self.base_damage = base_damage

    def attack(self):
        print(f"{self.race} наносит обычный удар на {self.base_damage} урона.")

    def get_status(self):
        print(f"{self.name} ({self.race}) - уровень {self.level}, здоровье: {self.health}")

class Mage(Character):
    def attack(self):
        damage = self.base_damage + self.level * 5
        print(f"{self.name} кастует фаербол и наносит {damage} магического урона")

class Berserk(Character):
    def attack(self):
        damage = self.base_damage + self.level * 6
        print(f"{self.name} впадает в ярость и наносит {damage} урона своим топором")

jaina = Mage("Джайна","Человек", 7, 20)
jaina.get_status()
jaina.attack()

grom = Berserk("Громмаш", "Орк", 9, 22)
grom.get_status()
grom.attack()

# Попросить чат показать на этом же примеры принципы ООП
# 📌 Всё у тебя логично и грамотно идёт:
#
# общий Character
#
# наследники Mage, Berserker
#
# attack() переопределяешь под каждый класс
#
# Хочешь — добавим take_damage() и heal(), чтобы уже был боевой движ?
# Или эффект "ярости", когда мало HP?

# Хочешь — можем на этом примере построить:
#
# 🔄 взаимодействие между персонажами (атака, урон)
#
# 🧪 автотесты на базу классов (как в pytest)
#
# 🎮 или просто доделать RPG-логику: лечилки, криты, левелап
#
# Какой путь выбираешь?


