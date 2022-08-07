import json
import pandas as pd

# The start of being able to save data
# Right now, we're only passing whatever player data we currently have
# You can see all player data by typing 'save-test' within the game

#TODO: Data is saving to a json file, now we need a method to load that json file and set variables
def save_player_data(name, cur_energy, max_energy, cur_hp, max_hp, currency):
	
	data = {
		"name": name,
		"energy": cur_energy,
		"max_energy": max_energy,
		"hp": cur_hp,
		"max_hp": max_hp,
		"currency": currency
	}

	player_data_df = pd.DataFrame([data])

	player_data_df.to_json(r'player_data.json', orient='index')

# TODO: Save Skill data to another dataframe, merge both together.
