class Skill:
    def __init__(self, name):
        self.name = name
        self.current_xp = 0
        self.xp_to_next_lvl = 10
        self.current_level = 0

    def gain_xp(self, amount):
        self.current_xp += amount
        self.level_check()

    def level_check(self):
        if self.current_xp >= self.xp_to_next_lvl:
            self.current_level += 1
            self.current_xp = 0
            self.xp_to_next_lvl *= 2
