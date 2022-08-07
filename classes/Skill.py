class Skill:
    def __init__(self, name):
        self.name = name
        self.xp = 0
        self.xp_to_level_up = 10
        self.level = 0

    def gain_xp(self, amount):
        self.xp += amount
        self.level_check()

    def level_check(self):
        if self.xp >= self.xp_to_level_up:
            self.level += 1
            self.xp = 0
            self.xp_to_level_up *= 2
