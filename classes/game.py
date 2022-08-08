import pygame
from config import COLORS
from classes.textboxes import TextBox

class Game:
	def __init__(self, w, h):
		self.w = w
		self.h = h
		self.screen = pygame.display.set_mode((w, h))
		pygame.display.set_caption('pyRPG')

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

	@staticmethod
	def display_stat(screen, stat_name, curr, max, x, y, w, h, color):
		# Increment this by height after printing a line
		curr_y = y

		# Display stat name
		text_box = TextBox(stat_name + ': ', COLORS["WHITE"], x, curr_y, w, h)
		screen.blit(text_box.rendered_text, text_box.rect)
		curr_y += h

		# Calculate dimensions for bar
		scale = w / max
		curr_width = scale * curr
		remaining_width = scale * (max - curr)

		# Create rectangles for bar
		curr_bar = pygame.Rect(x, curr_y, curr_width, h)
		remaining_bar = pygame.Rect(x + curr_width, curr_y, remaining_width, h)

		# Draw bars
		pygame.draw.rect(screen, color, curr_bar)
		pygame.draw.rect(screen, COLORS["BLACK"], remaining_bar)

		# Display current and max values
		text_box = TextBox(str(curr) + '/' + str(max), COLORS["WHITE"], x + w, curr_y, w, h)
		screen.blit(text_box.rendered_text, text_box.rect)


	def display_stats(self, screen, x, y):
		curr_y = y
		line_w = 100
		line_h = 30
		self.display_stat(
			screen,
			'HP', self.hp, self.max_hp,
			x, curr_y, line_w, line_h,
			COLORS["RED"]
		)
		# display_stat prints two lines, so we increment twice
		curr_y += line_h * 2
		self.display_stat(
			screen,
			'Energy', self.energy, self.max_energy,
			x, curr_y, line_w, line_h,
			COLORS["BLUE"]
		)


class Action:
	def __init__(
		self,
		name,
		type, # normal OR skill
		key, # pygame.key that is pressed
		char # shortcut displayed to player
	):
		self.name = name
		self.type = type
		self.key = key
		self.char = char

	# Render text for the actions shortcut and name at the given (x,y) position
	def display(self, screen, x, y):
		text_box = TextBox(self.char + ': ' + self.name, COLORS["WHITE"], x, y, 100, 50)
		screen.blit(text_box.rendered_text, text_box.rect)

	# Render text for all actions provided
	@staticmethod
	def display_all(screen, actions, x, y):
		for action in actions:
			action.display(screen, x, y)
			y += 50

ACTIONS = [
	Action("Mining", 'skill', pygame.K_m, 'M'),
	Action("Fishing", 'skill', pygame.K_f, 'F'),
	Action("Combat", 'skill', pygame.K_c, 'C'),
	Action("Rest", 'normal', pygame.K_r, 'R'),
	Action("Quit", 'normal', pygame.K_r, 'Q'),
]

class Skill:
	def __init__(self, name):
		self.name = name
		self.xp = 0
		self.xp_to_level_up = 10
		self.level = 0

	def gain_xp(self, amount):
		self.xp += amount
		self.level_check()

	# Check if skill should be leveled up
	def level_check(self):
		if self.xp >= self.xp_to_level_up:
			self.level += 1
			self.xp = 0
			self.xp_to_level_up *= 2

	# Render text for skill name and level
	def display(self, screen, x, y, w, h):
		text_box = TextBox(self.name + " Lvl. " + str(self.level), COLORS["WHITE"], x, y, 100, 50)
		screen.blit(text_box.rendered_text, text_box.rect)

	# Render progress bar for skill experience
	def display_bar(self, screen, x, y, w, h):
		scale = w / self.xp_to_level_up
		earned_width = scale * self.xp
		remaining_width = scale * (self.xp_to_level_up - self.xp)
		earned_bar = pygame.Rect(x, y, earned_width, h)
		remaining_bar = pygame.Rect(x + earned_width, y, remaining_width, h)
		pygame.draw.rect(screen, COLORS["WHITE"], earned_bar)
		pygame.draw.rect(screen, COLORS["GREY"], remaining_bar)

	# Render text and bar for all skills provided
	def display_all(screen, skills, x, y):
		curr_y = y
		line_w = 100
		line_h = 30
		for skill in skills:
			skill.display(screen, x, curr_y, line_w, line_h)
			curr_y += line_h
			skill.display_bar(screen, x, curr_y, line_w, line_h)
			curr_y += line_h

