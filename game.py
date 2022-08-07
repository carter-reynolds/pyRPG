import random as rand
import platform
import os
from classes.Player import Player
from classes.Skill import Skill
from savegame import save_player_data, save_skill_data
from termcolor import colored, cprint
from messages import random_rest_messages, random_mine_messages, random_fish_messages, random_combat_messages


'''
This is a little 'game' I am making that is supposed to be a text-based survival game. 
There is little actual functionality currently, but there will be more eventually.

Currently, this script probably only runs properly on Mac as the environment variables
are specific to xterm-256color which is the Mac terminal. 

Windows support to come at a later time.
'''


# TODO: USE THESE
environment_variables = {
    "current_temp": 75,
    "min_max_temp": [20, 110],
    "time_of_day": ["morning", "midday", "evening", "night"],
    "weather": ["sunny", "light_rain", "storm", "snow"]
}

def clear_term():
    system_type = platform.system()

    if system_type == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def print_bar(title, curr, max, level, color='white'):
    if level is None:
        level_text = ""
    else:
        level_text = " Lvl. " + str(level)

    scale = 0.2 if 'Health' in title else 1
    # substrings to build output
    progress_earned = int(curr * scale) * '\u2588'
    progress_remaining = int((max - curr) * scale) * '\u2591'
    print(title + level_text)
    cprint(progress_earned + progress_remaining + ' ' + str(curr) + '/' + str(max) + '\n', color)


'''
get_cur_stats():
In order to avoid constantly retyping out the stats I need to display after every action
We will just use a function that gets called after every action instead cuz efficient?

Not sure why the dictionaries used here didn't have to be 'global'? 
>> Is it because this function runs within a function that already has the global access?
'''


def get_cur_stats(skills_list, player):

    print_bar('Energy', player.current_energy, player.max_energy, None, 'blue')
    print_bar('Health', player.current_hp, player.max_hp, None, 'red')

    print(colored('Player Experience: \n', 'yellow', attrs=['bold', 'underline']))

    for skill in skills_list:
        print_bar(skill.name, skill.current_xp, skill.xp_to_next_lvl, skill.current_level)

    print('\n')

def title_text():
    welcome_text = 'pyRPG: A text-based RPG that no one asked for!'
    box_char = '*'
    print(box_char*(len(welcome_text)+4))
    print(box_char,welcome_text,box_char)
    print(box_char*(len(welcome_text)+4), '\n\n')


# This is most of the game's logic within a single function - please don't judge me
def game_main():

    title_text()

    player_name_input = input("What is your characters name?:")

    player = Player(player_name_input)

    skills_list = [
        Skill("Mining"),
        Skill("Fishing"),
        Skill("Combat")
    ]
    
    # These are the only input values that can be used in the game currently
    valid_inputs = ["rest", "mine", "fish", "combat", "save-test", "actions"]

    while True:  # Keeps the game going after every action (always truthy unless error)
        
        get_input = input("What action do you want to perform? (Type: 'actions' to display actions.)\n\n")
        
        clear_term()
        title_text()
        if player.current_energy > 0:
            if get_input in valid_inputs:
                if get_input == "rest":

                    message_rest = random_rest_messages[(rand.randint(0, 4))]
                    print(message_rest, '\n')

                    player.rest()

                    get_cur_stats(skills_list, player)

                elif get_input == "save-test":
                    save_player_data(
                        player.name, 
                        player.current_energy,
                        player.max_energy,
                        player.current_hp,
                        player.max_hp,
                        player.currency
                    )
                    save_skill_data(
                        skills_list
                    )

                elif get_input == "actions":

                    print('Action List: \n', valid_inputs, '\n')

                    get_cur_stats(skills_list, player)

                elif get_input == "mine":

                    message_mine = random_mine_messages[(rand.randint(0,4))]
                    print(message_mine, '\n')
                    
                    player.lose_energy(1)

                    for skill in skills_list:
                        if skill.name == "Mining":
                            skill.gain_xp(1)

                    get_cur_stats(skills_list, player)

                elif get_input == "fish":

                    message_fish = random_fish_messages[(rand.randint(0,4))]
                    print(message_fish, '\n')

                    player.lose_energy(1)

                    for skill in skills_list:
                        if skill.name == "Fishing":
                            skill.gain_xp(1)

                    get_cur_stats(skills_list, player)

                elif get_input == "combat":

                    message_combat = random_combat_messages[(rand.randint(0,4))]
                    print(message_combat, '\n')

                    player.lose_energy(1)

                    for skill in skills_list:
                        if skill.name == "Combat":
                            skill.gain_xp(1)

                    get_cur_stats(skills_list, player)

            else:
                cprint("Not a Valid Input! Try again.", 'red')
                
        elif player.current_energy == 0 and get_input != "rest":
            cprint("You are too tired. Consider resting!", 'red')

        else:   
            message_rest = random_rest_messages[(rand.randint(0, 4))]
            print(message_rest)

            player.rest()
            get_cur_stats(skills_list, player)

clear_term()    # Clear the terminal for new game        
game_main()     # Start the game

