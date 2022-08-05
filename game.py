import random as rand
import time
from termcolor import colored, cprint
from playsound import playsound
import os
import sys

'''
This is a little 'game' I am making that is supposed to be a text-based survival game. 
There is little actual functionality currently, but there will be more eventually.

Currently, this script probably only runs properly on Mac as the environment variables
are specific to xterm-256color which is the Mac terminal. 

Windows and Linux support to come at a later time.
'''

os.system('clear') # Start with a fresh terminal

# I think I need this to clear terminal properly. Unsure but here it is anyways
# Likely entirely broken for Windows, but easily handable

#TODO: Add Windows CMD Prompt/Powershell Support
os.environ['TERM'] = 'xterm-256color'   # Mac Term only

# Common Value Dictionaries
skill_lvl = {
    "mining":0,
    "fishing":0,
    "combat":0
}

xp = {
    "mining":0,
    "fishing":0,
    "combat":0
}

ply = {
    "energy": 24,
    "hp": 100
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

# Create Random Rest Action Messages
random_rest_messages = [
    "You stare into the fire as time passes longer into the day...",                  # 0 index
    "You feel the wind brush your skin as you sit and ponder your previous actions.", # 1 index
    "You have decided it's better to rest right now.",                                # 2 index
    "You decided to take a breather.",                                                # 3 index
    "You rest for 1 hour."                                                            # 4 index
    ]

# Create Random Mining Action Messages
random_mine_messages = [
    "You mine for 1 hour.",
    "You strike the rock with force!",
    "You swing your pickaxe.",
    "** loud pickaxe sounds **",
    "You mine the rock hoping to find something of use..."
    ]
    
# Create Random Fishing Action Messages   
random_fish_messages = [
    "You cast your line into the water.",
    "You cast your line hoping to get some dinner tonight.",
    "You never did like fishing that much...",
    "You wait for a bite on your fishing line.",
    "You fish for 1 hour."
    ]
    
# Create Random Combat Action Messages
random_combat_messages = [
    "COMBAT: Take that, scum! HE-YAH!",
    "COMBAT: Your steel strikes the enemy hard and true.",
    "COMBAT: You get into a scuffle with a foe.",
    "COMBAT: *Weapons and Combat Sounds*",
    "COMBAT: You thrust your weapon."
    ]
    
random_mine_sounds = ["sounds/pickaxe1.wav", "sounds/pickaxe2.wav"]
random_fish_sounds = ["sounds/fishing1.wav", "sounds/fishing2.wav"]
    



def level_check():
    
    global xp
    global skill_lvl
    global xp_to_next_lvl
    
    
    os.system('clear') # Clean the terminal again!
    
    cprint('You sit down to ponder everything you\'ve learned up to this point..... \n', 'yellow')
    
    time.sleep(3)
    
    if xp['mining'] >= xp_to_next_lvl['mining']:
        skill_lvl['mining'] += 1
        mine_exp_new = xp['mining'] - xp_to_next_lvl['mining']
        xp['mining'] = mine_exp_new
        xp_to_next_lvl['mining'] += xp_to_next_lvl['mining']
        
        cprint('Mining Leveled up to: ' + str(skill_lvl['mining']) + '\n', 'green')
        cprint('Next Level up at: ' + str(xp_to_next_lvl['mining']) + ' XP\n', 'green')
        
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
        
        crint('Combat Leveled up to: ' + str(skill_lvl['combat']) + '\n', 'green')
        cprint('Next Level up at: ' + str(xp_to_next_lvl['combat']) + ' XP\n', 'green')
        
    else:
        cprint('XP not high enough for level up this time!' + '\n', 'red')

'''
In order to avoid constantly retyping out the stats I need to display after every action
We will just use a function that gets called after every action instead cuz efficient?
'''
def get_cur_stats():
    print('Energy: ', ply['energy'])
    print('Health: ', ply['hp'], '\n')
    
    cprint('Player Experience:', 'yellow')
    print('Mining XP: ', xp['mining'])
    print('Fishing XP: ', xp['fishing'])
    print('Combat XP: ', xp['combat'], '\n')
    
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
    

    while True: # Keeps the game going after every action (always truthy unless error)
        
        get_input = input("What Action Are You Doing? (rest, mine, fish, combat)\n\n")
        os.system('clear') # Clean the terminal again!
        
        if ply['energy'] > 0: # If player_energy is greater than 0, keep going
        
            if get_input in valid_inputs: # If input is in valid_inputs, keep going
            
                if get_input == "rest": 
                    
                    # Display a random rest message
                    message_rest = random_rest_messages[(rand.randint(0,4))]
                    print(message_rest, '\n')
                    
                    ply['energy'] += 1
                    
                    #Check for possible level increases
                    level_check()
                    
                    #Show full stats
                    get_cur_stats()
                    
                    
                elif get_input == "mine":
                    
                    #Display a random mine message
                    message_mine = random_mine_messages[(rand.randint(0,4))]
                    print(message_mine, '\n')
                    
                    # Play a random related sound
                    sound_mine = random_mine_sounds[(rand.randint(0,1))]
                    # playsound(sound_mine)
                    
                    #Decrease energy by 1, increase mining XP by 1, display full stats
                    ply['energy'] -= 1
                    xp['mining'] += 1 

                    get_cur_stats()
                    
                    
                elif get_input == "fish":
                    
                    #Display random fish message
                    message_fish = random_fish_messages[(rand.randint(0,4))]
                    print(message_fish, '\n')
                    
                    # Play a random related sound
                    sound_fish = random_fish_sounds[(rand.randint(0,1))]
                    # playsound(sound_fish)
                    
                    ply['energy'] -= 1
                    xp['fishing'] += 1

                    get_cur_stats()
                    
                
                elif get_input == "combat": # Should rename to "combat" instead?

                    message_combat = random_combat_messages[(rand.randint(0,4))]
                    print(message_combat, '\n')

                    ply['energy'] -= 1
                    xp['combat'] += 1 # Add 1 to Combat XP

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
     
game_main() # Starts the game
