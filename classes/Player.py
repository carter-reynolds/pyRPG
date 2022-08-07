class Player:
    def __init__(self, name):
        self.name = name
        self.energy = 24
        self.max_energy = 24
        self.hp = 100
        self.max_hp = 100
        self.currency = 0

    def gain_energy(self, amount):
        self.energy += amount

    def lose_energy(self, amount):
        self.energy -= amount

    def rest(self):
        self.energy = self.max_energy
