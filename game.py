import random as rand
import time
from termcolor import colored, cprint
from playsound import playsound
from messages import random_rest_messages, random_mine_messages, random_fish_messages, random_combat_messages
import os

'''
This is a little 'game' I am making that is supposed to be a text-based survival game. 
There is little actual functionality currently, but there will be more eventually.

Currently, this script probably only runs properly on Mac as the environment variables
are specific to xterm-256color which is the Mac terminal. 

Windows support to come at a later time.
'''

os.system('clear')  # Start with a fresh terminal

# TODO: Add Windows CMD Prompt/Powershell Support
os.environ['TERM'] = 'xterm-256color'

# Common Value Dictionaries
skill_lvl = {
    "mining": 0,
    "fishing": 0,
    "combat": 0
}

xp = {
    "mining": 0,
    "fishing": 0,
    "combat": 0
}

ply = {
    "energy": 24,
    "max_energy": 24,
    "hp": 100,
    "max_hp": 100
}

xp_to_next_lvl = {
    "mining": 10,
    "fishing": 10,
    "combat": 10
}

# TODO: USE THESE
environment_variables = {
    "current_temp": 75,
    "min_max_temp": [20, 110],
    "time_of_day": ["morning", "midday", "evening", "night"],
    "weather": ["sunny", "light_rain", "storm", "snow"]
    }


'''
The next four tables are used to set up random messages that will appear every
time an action is taken by a player. We use a random int to tell the game which
message to ultimately display so it's entirely random
'''
    
random_mine_sounds = ["sounds/pickaxe1.wav", "sounds/pickaxe2.wav"]
random_fish_sounds = ["sounds/fishing1.wav", "sounds/fishing2.wav"]
    
'''
level_check():
Runs a check during every "rest" action to attempt and convert gained XP into a new level of any various skill.
'''


def level_check():
    
    global xp
    global skill_lvl
    global xp_to_next_lvl

    os.system('clear')  # Clean the terminal again!
    
    cprint('You sit down to ponder everything you\'ve learned up to this point..... \n', 'yellow')
    
    time.sleep(3)  # Displays the above message on the screen for 3 seconds

    '''
    The next IFs are for converting XP per skill into a new level of any given skill
    '''

    if xp['mining'] >= xp_to_next_lvl['mining']:  # If current amount of mining xp > what is required for next level..
        skill_lvl['mining'] += 1                                # Add mining +1 to mining level
        mine_exp_new = xp['mining'] - xp_to_next_lvl['mining']  # current skill xp - xp spent to level up = mine_exp_new
        xp['mining'] = mine_exp_new                             # Set that as the new amount of xp
        xp_to_next_lvl['mining'] += xp_to_next_lvl['mining']    # Double the next level xp requirement (plan to balance)
        
        cprint('Mining Leveled up to: ' + str(skill_lvl['mining']) + '\n', 'green')  # Tell the player they leveled up
        cprint('Next Level up at: ' + str(xp_to_next_lvl['mining']) + ' XP\n', 'green')  # Print how much XP to next lvl
        
    elif xp['fishing'] >= xp_to_next_lvl['fishing']:
        skill_lvl['fishing'] += 1
        fish_exp_new = xp['fishing'] - xp_to_next_lvl['fishing']
        xp['fishing'] = fish_exp_new
        xp_to_next_lvl['fishing'] += xp_to_next_lvl['fishing']
        
        cprint('Fishing Leveled up to: ' + str(skill_lvl['fishing']) + '\n', 'green')
        cprint('Next Level up at: ' + str(xp_to_next_lvl['fishing']) + ' XP\n', 'green')
        
    elif xp['combat'] >= xp_to_next_lvl['combat']:
        skill_lvl['combat'] += 1
        combat_exp_new = xp['combat'] - xp_to_next_lvl['combat']
        xp['combat'] = combat_exp_new
        xp_to_next_lvl['combat'] += xp_to_next_lvl['combat']
        
        cprint('Combat Leveled up to: ' + str(skill_lvl['combat']) + '\n', 'green')
        cprint('Next Level up at: ' + str(xp_to_next_lvl['combat']) + ' XP\n', 'green')
        
    else:
        cprint('XP not high enough for level up this time!' + '\n', 'red')


'''
Helper functions to print progress bars for the experience levels
'''


def print_bar(title, curr, max, color='white'):
    scale = 0.2 if 'Health' in title else 1
    # substrings to build output
    progress_earned = int(curr * scale) * '\u2588'
    progress_remaining = int((max - curr) * scale) * '\u2591'
    print(title)
    cprint(progress_earned + progress_remaining + ' ' + str(curr) + '/' + str(max) + '\n', color)


'''
get_cur_stats():
In order to avoid constantly retyping out the stats I need to display after every action
We will just use a function that gets called after every action instead cuz efficient?

Not sure why the dictionaries used here didn't have to be 'global'? 
>> Is it because this function runs within a function that already has the global access?
'''


def get_cur_stats():
    print_bar('Energy: ', ply['energy'], ply['max_energy'], 'blue')
    print_bar('Health: ', ply['hp'], ply['max_hp'], 'red')
    
    cprint('Player Experience:', 'yellow')
    print_bar('Mining XP: ', xp['mining'], xp_to_next_lvl['mining'])
    print_bar('Fishing XP: ', xp['fishing'], xp_to_next_lvl['fishing'])
    print_bar('Combat XP: ', xp['combat'], xp_to_next_lvl['combat'])
    
    cprint('Player Levels:', 'yellow')
    print('Mining Level: ', skill_lvl['mining'])
    print('Fishing Level: ', skill_lvl['fishing'])
    print('Combat Level: ', skill_lvl['combat'], '\n')

    
# This is most of the game's logic within a single function - please don't judge me
def game_main():

    global ply
    global xp
    global skill_lvl
    global xp_to_next_lvl
    
    # These are the only input values that can be used in the game currently
    valid_inputs = ["rest", "mine", "fish", "combat"]

    while True:  # Keeps the game going after every action (always truthy unless error)

        get_input = input("What Action Are You Doing? (rest, mine, fish, combat)\n\n")
        os.system('clear')  # Clean the terminal again!
        
        if ply['energy'] > 0:  # If player_energy is greater than 0, keep going
        
            if get_input in valid_inputs:  # If input is in valid_inputs, keep going
            
                if get_input == "rest": 
                    
                    # Display a random rest message
                    message_rest = random_rest_messages[(rand.randint(0, 4))]
                    print(message_rest, '\n')
                    
                    ply['energy'] += 1
                    
                    # Check for possible level increases
                    level_check()
                    
                    # Show full stats
                    get_cur_stats()

                elif get_input == "mine":
                    
                    # Display a random mine message
                    message_mine = random_mine_messages[(rand.randint(0,4))]
                    print(message_mine, '\n')
                    
                    # Play a random related sound
                    sound_mine = random_mine_sounds[(rand.randint(0,1))]
                    # playsound(sound_mine)
                    
                    # Decrease energy by 1, increase mining XP by 1, display full stats
                    ply['energy'] -= 1
                    xp['mining'] += 1 

                    get_cur_stats()

                elif get_input == "fish":
                    
                    # Display random fish message
                    message_fish = random_fish_messages[(rand.randint(0,4))]
                    print(message_fish, '\n')
                    
                    # Play a random related sound
                    sound_fish = random_fish_sounds[(rand.randint(0,1))]
                    # playsound(sound_fish)
                    
                    ply['energy'] -= 1
                    xp['fishing'] += 1

                    get_cur_stats()

                elif get_input == "combat":

                    message_combat = random_combat_messages[(rand.randint(0,4))]
                    print(message_combat, '\n')

                    ply['energy'] -= 1
                    xp['combat'] += 1  # Add 1 to Combat XP

                    get_cur_stats()

            else:
                cprint("Not a Valid Input! Try again.", 'red')
                
        elif ply['energy'] == 0 and get_input != "rest":
            cprint("You are too tired. Consider resting!", 'red') 
            
        else:   
            message_rest = random_rest_messages[(rand.randint(0,4))]
            print(message_rest)

            ply['energy'] += 1  
            level_check()
            get_cur_stats()                     


game_main()  # Starts the game
