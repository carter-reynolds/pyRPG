class Player:
    def __init__(self, name):
        self.name = name
        self.current_energy = 24
        self.max_energy = 24
        self.current_hp = 100
        self.max_hp = 100
        self.currency = 0

    def gain_energy(self, amount):
        self.current_energy += amount

    def rest(self):
        self.current_energy = self.max_energy
