import json
import pandas as pd

# The start of being able to save data
# Right now, we're only passing whatever player data we currently have
# You can see all player data by typing 'save-test' within the game

#TODO: Data is saving to a json file, now we need a method to load that json file and set variables
def save_player_data(player):
	data_player = {
		"name": player.name,
		"energy": player.energy,
		"max_energy": player.max_energy,
		"hp": player.hp,
		"max_hp": player.max_hp,
		"currency": player.currency
	}

	player_data_df = pd.DataFrame([data_player])

	print('Player data to save: \n', player_data_df, '\n')

	player_data_df.to_json(r'./save/player_data.json', orient='index')

def save_skill_data(skills):

	date_skills = []

	for skill in skills:
		date_skills.append(
			{
				"skill_name":skill.name,
				"skill_current_xp": skill.current_xp,
				"skill_xp_to_next_level": skill.xp_to_next_lvl,
				"skill_current_level": skill.current_level
			}
		)

	skill_data_df = pd.DataFrame(date_skills)

	print('Skill data to save: \n', skill_data_df)

	skill_data_df.to_json(r'./save/skill_data.json', orient='index')
