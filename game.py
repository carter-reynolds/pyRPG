import random as rand
import globals.py 
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

# Level and Experience Variables I will need - currently 3 tables
# TODO: Using a dictionary may be better to match keys and values easier than remembering indexes
player_skills = ["Mining","Fishing","Combat"]
player_level = [0, 0, 0]
player_exp = [0, 0, 0]

# Revelant Indexes for Changing Values:
# 0 - Mining
# 1 - Fishing
# 2 - Combat

# Assigning Some Default Variables
player_energy = 20      # How much energy we start with
player_health = 50      # How much health we start with (unused currently)
hours_of_day_left = 16  # Default hours in a day (unused currently)

# Level Stuff
mine_xp_required = 3
fish_xp_required = 3
combat_xp_required = 3

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
    
    global mine_xp_required
    global fish_xp_required
    global combat_xp_required
    
    os.system('clear') # Clean the terminal again!
    
    cprint('You sit down to ponder everything you\'ve learned up to this point..... \n', 'yellow')
    
    time.sleep(3)
    
    if player_exp[0] >= mine_xp_required:
        player_level[0] += 1
        mine_exp_new = player_exp[0] - mine_xp_required
        player_exp[0] = mine_exp_new
        mine_xp_required += mine_xp_required
        
        cprint('Mining Leveled up to: ' + str(player_level[0]) + '\n', 'green')
        cprint('Next Level up at: ' + str(mine_xp_required) + ' XP\n', 'green')
        
    elif player_exp[1] >= fish_xp_required:
        player_level[1] += 1
        fish_exp_new = player_exp[1] - fish_xp_required
        player_exp[1] = fish_exp_new
        fish_xp_required += fish_xp_required
        
        cprint('Fishing Leveled up to: ' + str(player_level[1]) + '\n', 'green')
        cprint('Next Level up at: ' + str(fish_xp_required) + ' XP\n', 'green')
        
    elif player_exp[2] >= combat_xp_required:
        player_level[2] += 1
        combat_exp_new = player_exp[2] - combat_xp_required
        player_exp[2] = combat_exp_new
        combat_xp_required += combat_xp_required
        
        print('Combat Leveled up to: ' + str(player_level[2]) + '\n', 'green')
        cprint('Next Level up at: ' + str(combat_xp_required) + ' XP\n', 'green')
        
    else:
        cprint('XP not high enough for level up this time!' + '\n', 'red')

'''
In order to avoid constantly retyping out the stats I need to display after every action
We will just use a function that gets called after every action instead cuz efficient?
'''
def get_cur_stats():
    print('Energy: ', player_energy)
    print('Health: ', player_health, '\n')
    
    print('Player Experience:')
    print('Mining XP: ', player_exp[0])
    print('Fishing XP: ', player_exp[1])
    print('Combat XP: ', player_exp[2], '\n')
    
    print('Player Levels:')
    print('Mining Level: ', player_level[0])
    print('Fishing Level: ', player_level[1])
    print('Combat Level: ', player_level[2], '\n')
    

        
    
# This is most of the game's logic within a single function - please don't judge me
def game_main():
    
     # These are the only input values that can be used in the game currently
    valid_inputs = ["rest", "mine", "fish", "combat"]
    
    '''
    These next 3 variables are global because they are established initially outside
    the scope of this function. There is probably a better way to do this, but it worked
    and I did not want to mess with it more yet.
    '''
    
    global player_energy 
    global player_health
    global player_level
    
    
    while True: # Keeps the game going after every action (always truthy unless error)
        
        get_input = input("What Action Are You Doing? (rest, mine, fish, combat)\n\n")
        os.system('clear') # Clean the terminal again!
        
        if player_energy > 0: # If player_energy is greater than 0, keep going
        
            if get_input in valid_inputs: # If input is in valid_inputs, keep going
            
                if get_input == "rest": 
                    
                    # Display a random rest message
                    message_rest = random_rest_messages[(rand.randint(0,4))]
                    print(message_rest, '\n')
                    
                    
                    #Increase energy by 1 for resting
                    player_energy = player_energy + 1
                    
                    #Check for possible level increases
                    level_check()
                    
                    #Show full stats
                    get_cur_stats()
                    
                    
                elif get_input == "mine":
                    
                    
                    #Display a random mine message
                    message_mine = random_mine_messages[(rand.randint(0,4))]
                    print(message_mine, '\n')
                    
                    # Play a random related sound
                    #sound_mine = random_mine_sounds[(rand.randint(0,1))]
                    #playsound(sound_mine)
                    
                    #Decrease energy by 1, increase mining XP by 1, display full stats
                    player_energy = player_energy - 1
                    player_exp[0] = player_exp[0] + 1 
                    get_cur_stats()
                    
                    
                elif get_input == "fish":
                    
                    
                    #Display random fish message
                    message_fish = random_fish_messages[(rand.randint(0,4))]
                    print(message_fish, '\n')
                    
                    # Play a random related sound
                    #sound_fish = random_fish_sounds[(rand.randint(0,1))]
                    #playsound(sound_fish)
                    
                    #Decrease energy by 1, increase fishing XP by 1, display full stats
                    player_energy = player_energy - 1
                    player_exp[1] = player_exp[1] + 1 
                    get_cur_stats()
                    
                
                elif get_input == "combat": # Should rename to "combat" instead?
                    message_combat = random_combat_messages[(rand.randint(0,4))]
                    print(message_combat, '\n')
                    player_energy = player_energy - 2
                    player_exp[2] = player_exp[2] + 3 # Add 1 to Combat XP
                    get_cur_stats()
                    
                    
            else:
                cprint("Not a Valid Input! Try again.", 'red')
                
        elif player_energy == 0 and get_input != "rest":
            cprint("You are too tired. Consider resting!", 'red') 
            
        else:   
            message_rest = random_rest_messages[(rand.randint(0,4))]
            print(message_rest)
            player_energy = player_energy + 1  
            level_check()
            get_cur_stats()                     
     
game_main() # Starts the game
        
        


