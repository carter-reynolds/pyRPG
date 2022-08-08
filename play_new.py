import pygame
successes, failures = pygame.init()

from classes.game import Game, Player, Skill, Action, ACTIONS
from classes.textboxes import TEXT_BOXES
from config import MODES, COLORS

print("Initializing pygame: {0} successes and {1} failures.".format(successes, failures))

# Create new game
game = Game(1000, 1000)

# Init skills
skills_list = [
	Skill("Mining"),
	Skill("Fishing"),
	Skill("Combat")
]

# These are the only input values that can be used in the game currently
valid_inputs = ["rest", "mine", "fish", "combat", "save-test", "actions"]

player = None
running = True
mode = MODES["START"]
while mode is not MODES["QUIT"]:
	game.screen.fill(COLORS["BLACK"])  # Fill the screen with background color.

	##### PROCESS EVENTS #####
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			mode = MODES["QUIT"]

		if mode == MODES["START"]:

			if event.type == pygame.KEYDOWN:

				# Create player and start game
				if event.key == pygame.K_RETURN:
					player = Player(TEXT_BOXES["NAME_INPUT"].text)
					mode = MODES["PLAYING"]

				# Remove last char
				elif event.key == pygame.K_BACKSPACE:
					TEXT_BOXES["NAME_INPUT"].backspace()

				# Add pressed key to input text
				else:
					TEXT_BOXES["NAME_INPUT"].append(event.unicode)

		if mode == MODES["PLAYING"]:
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_q:
					mode = MODES["QUIT"]
					break
				for action in ACTIONS:
					if event.key == action.key: # Find action that matches current key press
						if (action.type == 'normal'): # Check action type
							if (action.name == 'Rest'):
								player.rest()
								break
							elif (action.name == 'Quit'):
								mode = MODES["QUIT"]
								break
						elif (action.type == 'skill'):
							player.lose_energy(1) # Lose energy for each skill action
							for skill in skills_list:
								if skill.name == action.name:
									skill.gain_xp(1) # Gain xp for this skill
									break


	##### RENDER SCREEN #####
	if mode == MODES["START"]:
		TEXT_BOXES["NAME_PROMPT"].display(game.screen)
		TEXT_BOXES["NAME_INPUT"].display(game.screen)

	if mode == MODES["PLAYING"]:
		player.display_stats(game.screen, 0, 0)
		Skill.display_all(game.screen, skills_list, 0, 150)
		Action.display_all(game.screen, ACTIONS, 0, 350)
	

	pygame.display.update()  # Or pygame.display.flip()

print("Exited the game loop. Game will quit...")
quit()  # Not actually necessary since the script will exit anyway.