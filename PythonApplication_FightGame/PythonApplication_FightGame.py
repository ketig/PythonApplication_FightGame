import random

class Character:
    def __init__(self, name, health, attack_power):
        self._name = name
        self._health = health
        self._attack_power = attack_power

    @property
    def name(self):
        return self._name

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        self._health = max(0, value)

    def attack(self, opponent):
        damage = random.randint(1, self._attack_power)
        opponent.health -= damage
        print(f"{self.name} attacks {opponent.name} for {damage} damage!\n")

    def __str__(self):
        return f"{self.name} (Health: {self.health}, Attack Power: {self._attack_power})"


class Player(Character):
    def __init__(self, name, health, attack_power, gold=0):
        super().__init__(name, health, attack_power)
        self._gold = gold

    @property
    def gold(self):
        return self._gold

    def collect_gold(self, amount):
        self._gold += amount
        print(f"{self.name} has collected {amount} gold!\n")

    def __str__(self):
        return f"{super().__str__()} (Gold: {self.gold})"


class Enemy(Character):
    def __init__(self, name, health, attack_power, gold_reward):
        super().__init__(name, health, attack_power)
        self._gold_reward = gold_reward

    def defeated(self):
        print(f"{self.name} is defeated!\n")
        return self._gold_reward

    def __str__(self):
        return f"{super().__str__()} (Gold Reward: {self._gold_reward})"


class Game:
    def __init__(self, player):
        self._player = player
        self._enemies = []

    def add_enemy(self, enemy):
        self._enemies.append(enemy)

    def play(self):
        print(f"Welcome, {self._player.name}!\n")

        while self._enemies:
            enemy = random.choice(self._enemies)
            print(f"A wild {enemy.name} appears!\n")

            while self._player.health > 0 and enemy.health > 0:
                print(self._player)
                print(enemy)
                self._player.attack(enemy)
                if enemy.health <= 0:
                    gold = enemy.defeated()
                    self._player.collect_gold(gold)
                    self._enemies.remove(enemy)
                    break
                enemy.attack(self._player)
                if self._player.health <= 0:
                    print(f"{self._player.name} has been defeated!\nGame over.\n")
                    return

        print(f"Congratulations, {self._player.name}! You have defeated all enemies and won the game with {self._player.gold} gold.\n")

player = Player("Hero", 30, 10)

enemy1 = Enemy("Goblin", 15, 5, 10)
enemy2 = Enemy("Orc", 20, 7, 15)
enemy3 = Enemy("Dragon", 40, 12, 50)

game = Game(player)
game.add_enemy(enemy1)
game.add_enemy(enemy2)
game.add_enemy(enemy3)

game.play()
