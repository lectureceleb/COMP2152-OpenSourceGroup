# Import the random library to use for the dice later
import random

# Put all the functions into another file and import them
import functions

# Define two Dice
small_dice_options = list(range(1, 7))
big_dice_options = list(range(1, 21))

# Define the Weapons
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear Bomb"]

# Define the Loot
loot_options = ["Health Potion", "Poison Potion", "Secret Note", "Leather Boots", "Flimsy Gloves"]
belt = []

# Define the Monster's Powers
monster_powers = {
    "Fire Magic": 2,
    "Freeze Time": 4,
    "Super Hearing": 6
}

# Define the available dragons as dictionaries
dragons_den = [
    {"name": "Blaze", "element": "Fire", "role": "Attack"},
    {"name": "Smaug", "element": "Earth", "role": "Shield"},
    {"name": "Drogon", "element": "Air", "role": "Attack"},
    {"name": "Falkor", "element": "Water", "role": "Shield"}
]

# Randomly select up to 3 dragons using list comprehension
hero_dragons = random.sample(dragons_den, min(3, len(dragons_den)))

# Define the number of stars to award the player
num_stars = 0

# Loop to get valid input for Hero and Monster's Combat Strength
i = 0
input_invalid = True

while input_invalid and i in range(5):
    print("    ------------------------------------------------------------------")
    print("    |", end="    ")
    combat_strength = input("Enter your combat Strength (1-6): ")
    print("    |", end="    ")
    m_combat_strength = input("Enter the monster's combat Strength (1-6): ")

    # Validate input: Check if the string inputted is numeric
    if (not combat_strength.isnumeric()) or (not m_combat_strength.isnumeric()):
        # If one of the inputs are invalid, print error message and halt
        print("    |    One or more invalid inputs. Player needs to enter integer numbers for Combat Strength    |")
        i = i + 1
        continue

    # Note: Now safe to cast combat_strength to integer
    # Validate input: Check if the string inputted
    elif (int(combat_strength) not in range(1, 7)) or (int(m_combat_strength)) not in range(1, 7):
        print("    |    Enter a valid integer between 1 and 6 only")
        i = i + 1
        continue

    else:
        input_invalid = False
        break

if not input_invalid:
    input_invalid = False
    combat_strength = int(combat_strength)
    m_combat_strength = int(m_combat_strength)

    # Roll for weapon
    print("    |", end="    ")
    input("Roll the dice for your weapon (Press enter)")
    ascii_image5 = """
           .-------.    ______
          |   o   ||   ||     |
         |_______|o|  |o |  o  |
         | o     | | |   o|_____|
         |   o   |o/ |o   |o    |
         |     o |/   | o|  o  |
         '-------'     ||____o|         
            """

    print(ascii_image5)
    weapon_roll = random.choice(small_dice_options)

    # Limit the combat strength to 6
    combat_strength = min(6, (combat_strength + weapon_roll))
    print("    |    The hero\'s weapon is " + str(weapons[weapon_roll - 1]))

    # Call the function to adjust the combat strength
    functions.adjust_combat_strength(combat_strength, m_combat_strength)

    # Weapon Roll Analysis
    print("    ------------------------------------------------------------------")
    print("    |", end="    ")
    input("Analyze the Weapon roll (Press enter)")
    print("    |", end="    ")
    if weapon_roll <= 2:
        print("--- You rolled a weak weapon, friend")
    elif weapon_roll <= 4:
        print("--- Your weapon is meh")
    else:
        print("--- Nice weapon, friend!")

    # If the weapon rolled is not a Fist, print out "Thank goodness you didn't roll the Fist..."
    if weapons[weapon_roll - 1] != "Fist":
        print("    |    --- Thank goodness you didn't roll the Fist...")

    # Roll for player health points
    print("    |", end="    ")
    input("Roll the dice for your health points (Press enter)")
    health_points = random.choice(big_dice_options)
    print("    |    Player rolled " + str(health_points) + " health points")

    # Roll for monster health points
    print("    |", end="    ")
    input("Roll the dice for the monster's health points (Press enter)")
    m_health_points = random.choice(big_dice_options)
    print("    |    Player rolled " + str(m_health_points) + " health points for the monster")

    # Collect Loot
    print("    ------------------------------------------------------------------")
    print("    |    !!You find a loot bag!! You look inside to find 2 items:")
    print("    |", end="    ")
    input("Roll for first item (enter)")

    # Collect Loot First time
    loot_options, belt = functions.collect_loot(loot_options, belt)
    print("    ------------------------------------------------------------------")
    print("    |", end="    ")
    input("Roll for second item (Press enter)")

    # Collect Loot Second time
    loot_options, belt = functions.collect_loot(loot_options, belt)

    print("    |    You're super neat, so you organize your belt alphabetically:")
    belt.sort()
    print("    |    Your belt: ", belt)

    # Use Loot
    belt, health_points = functions.use_loot(belt, health_points)

    print("    ------------------------------------------------------------------")
    print("    |", end="    ")
    input("Analyze the roll (Press enter)")
    # Compare Player vs Monster's strength
    print("    |    --- You are matched in strength: " + str(combat_strength == m_combat_strength))

    # Check the Player's overall strength and health
    print("    |    --- You have a strong player: " + str((combat_strength + health_points) >= 15))

    # Roll for the monster's power
    print("    |", end="    ")
    input("Roll for Monster's Magic Power (Press enter)")
    ascii_image4 = """                                                                       
                                 @@@                        
                                 @@@@@@@            @@         
                                 @@@ @@@@@@    @@@@@@@@        
                                 @@@    @@@@@@@  @@@         
                                 @@@             @@@          
                                @@@@            @@@@          
                              @@@@@            @@@@           
                           @@@@                  @@@@         
                         @@@@@@@@@                @@@@        
                              @@@@@@@@              @@@       
                                 @@@@@     @@@@@@@@@@@@@      
                              @@@@@ @@@   @@@@                
                            @@@@@    @@@@@@@                  
                          @@@@@      @@@@@                    
                        @@@@          @@@                     
                      @@@@                                    
                    @@@@                                      
                  @@@@                                        
                @@@@                                          
              @@@@                                            
           @@@@@                                              
         @@@@@                                                
        @@@@                                                                                                                            
                                        """
    print(ascii_image4)
    power_roll = random.choice(["Fire Magic", "Freeze Time", "Super Hearing"])

    # Increase the monster’s combat strength by its power
    m_combat_strength += min(6, m_combat_strength + monster_powers[power_roll])
    print("    |    The monster's combat strength is now " + str(
        m_combat_strength) + " using the " + power_roll + " magic power")

    # Inception dream
    num_dream_lvls = -1  # Initialize the number of dream levels
    while (num_dream_lvls < 0 or num_dream_lvls > 3):
        # Call Recursive function
        print("    |", end="    ")
        num_dream_lvls = input("How many dream levels do you want to go down? (Enter a number 0-3)")
        # If the value entered was not an integer, set the number of dream levels to -1 and loop again 
        if ((num_dream_lvls == "")):
            num_dream_lvls = -1
            print("Number entered must be a whole number between 0-3 inclusive, try again")

        else:
            num_dream_lvls = int(num_dream_lvls)

            if ((num_dream_lvls < 0) or (num_dream_lvls > 3)):
                num_dream_lvls = -1
                print("Number entered must be a whole number between 0-3 inclusive, try again")
            elif (not num_dream_lvls == 0):
                health_points -= 1
                crazy_level = functions.inception_dream(num_dream_lvls)
                combat_strength += crazy_level
                print("combat strength: " + str(combat_strength))
                print("health points: " + str(health_points))
        print("num_dream_lvls: ", num_dream_lvls)
        print("m_health_points: ", str(m_health_points))

    # ---------------------------OMAR: WEATHER EFFECTS-----------------------------------

    # Number value assigned to each mode (used for value assignments)
    normal = 0
    extreme = 1

    # Weather condition options
    conditions = [
        {"name": "sunny", "term": "sun", "mode": normal, "affected": "hero", "effect": "up"},
        {"name": "windy", "term": "wind", "mode": normal, "affected": "hero", "effect": "down"},
        {"name": "rainy", "term": "rain", "mode": normal, "affected": "monster", "effect": "up"},
        {"name": "snowy", "term": "snow", "mode": normal, "affected": "monster", "effect": "down"},
        {"name": "foggy", "term": "fog", "mode": normal, "affected": "none", "effect": "none"},
        {"name": "heat wave", "term": "scorching heat", "mode": extreme, "affected": "both", "effect": "down"},
        {"name": "cursed", "term": "curse", "mode": extreme, "affected": "hero", "effect": "down"}]

    # Potential stats to be changed based on mode
    stat_statements = ["health points", "strength and health"]

    # Modifiers that stats will be changed by
    h_modifier = 2
    m_modifier = 2

    # User interaction begins:
    # React to user's dream level choice to make feature flow with the overall game
    print("    ------------------------------------------------------------------")
    if num_dream_lvls > 0:
        print("    |    You have woken up from your dream!")
    else:
        print("    |    Who needs sleep, anyway?")
    print("    |    Would you like to play on normal or extreme mode?", end=" ")

    # Validate user input to ensure either 'normal' or 'extreme' is chosen
    mode = ""
    valid_entry = False
    while not valid_entry:
        try:
            mode = input().lower()
            if not mode == "normal" and not mode == "extreme":
                raise ValueError("Please enter either 'normal' or 'extreme' to proceed:")
        except ValueError as ve:
            print(f"    |    {ve}", end=" ")
        else:
            valid_entry = True
    print("    |    ")

    # Set values based on the mode chosen
    if mode == "extreme":
        extreme = True
        stat = stat_statements[extreme]

        # Extract extreme conditions (mode = 2)
        short_list = [c for c in conditions if c["mode"] == extreme]
        print(f"    |    You are in EXTREME mode!  You might regret this...")
    else:
        extreme = False
        stat = stat_statements[normal]

        # Extract normal conditions (mode = 1)
        short_list = [c for c in conditions if c["mode"] == normal]
        print(f"    |    You are in normal mode.  A little boring, don't you think...?")

    # Choose a random weather condition form the short list
    weather_roll = random.choice(range(len(short_list)))
    weather = short_list[weather_roll]

    # Cursed will have a unique message; do not mention weather if so
    if not weather["name"] == "cursed":
        print(f"    |    ")
        print(f"    |    This wasn't in the weather report...")
        print(f"    |    As you move forward, you notice it is now a {weather["name"]} day.")
        print(f"    |    ")

    # The weather effects alter the hero and/or monster
    if extreme:
        if weather["affected"] == "both":
            print(f"    |    The {weather["term"]} is becoming unbearable...  Your {stat} have decreased.")
            # If hero's health is already at 1, do not make a change
            if health_points == 1:
                print("Your health is already dangerously low.  Be careful!")
            else:
                # If hero's health is above 1, ensure the lowest hero health can fall to is 1
                print(f"    |    Your {stat} went down from {health_points} to {max(1, health_points // 2)} and"
                      f" {combat_strength} to {max(1, combat_strength // 2)}!")
                health_points = max(1, (health_points // 2))
                combat_strength = max(1, combat_strength // 2)

            print(f"    |    \"Luckily\" for you, the monster is struggling as well.")
            # If monster's health is already 1, do not make a change
            if m_health_points == 1:
                print(f"The monster's health is already dangerously low.  The odds are in your favour!")
            else:
                # If monster's health is above 1, ensure the lowest monster health can go is 1 hp
                print(
                    f"    |    The monster's {stat} went down from {m_health_points} to {max(1, m_health_points // 2)}"
                    f" and {m_combat_strength} to {max(1, m_combat_strength // 2)}!")
                m_health_points = max(1, m_health_points // 2)
                m_combat_strength = max(1, m_combat_strength // 2)
        elif weather["affected"] == "hero":

            gnome = """
        ⠀⠀⠀⠀⠀⠀⠀⡴⠒⠒⠒⠒⠤⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠙⢄⠀⠀⠀⠀⠀⠑⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢣⠀⠀⠀⠀⠀⠀⢂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⢀⠎⠀⠀⠀⠀⠀⠀⠀⢂⠀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⢠⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⢢⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⢀⠞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⢦⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⡠⠔⠁⠤⠤⠄⠒⠀⠀⣉⣁⣀⣀⡀⠀⠀⠁⠢⠀⠀⠀⠀⠀
        ⠀⠀⠀⢸⠤⠄⣀⣤⠔⣦⣮⣍⠀⠀⠀⢠⣶⢬⡑⡶⡒⡺⠀⠀⠀⠀⠀
        ⠀⠀⠀⢇⢣⡰⢟⡇⠀⠉⢩⣄⠀⠀⠀⠀⣤⡈⠁⠃⢣⢸⠆⠀⠀⠀⠀
        ⠀⠀⠀⠈⣧⣿⠟⠆⠀⠀⠙⠟⠁⡄⠒⢬⡿⠋⠀⠸⠸⠟⠀⠀⠀⠀⠀
        ⠀⠀⠀⡠⠿⠵⡀⢆⠀⠀⢀⣀⣼⡶⠤⢶⣇⣀⠀⠀⠆⡇⠀⠀⠀⠀⠀
        ⠀⢰⠁⠀⠀⠀⠀⢱⠈⠛⠿⢛⡡⣔⣒⡠⢙⠵⢬⠉⢁⡇⠀⠀⠀⠀⠀
        ⠀⢸⣢⡀⠀⢀⣀⠜⡹⠀⣨⠃⠀⠀⢃⠀⠀⠩⡀⠀⠁⡏⢆⠀⠀⠀⠀
        ⣔⠏⠀⠀⠀⣀⢇⢰⠀⠎⣧⠀⠀⠀⢸⡄⠀⠀⢱⠀⢀⡷⣾⡶⠤⡀⠀
        ⡏⡀⠀⡉⠁⢀⢼⢆⢸⠀⣿⠀⠀⠀⡘⠀⢸⠀⢸⠀⣸⡁⢳⠜⣀⠜⠆
        ⠡⡑⡄⠤⠀⠤⡎⠀⠙⡄⠈⠀⠀⠰⠁⠀⡘⠀⠀⡤⠃⡔⠘⠀⡼⠒⡇
        ⠀⠈⢩⠉⢐⠚⠁⠀⠀⠈⠢⡄⠀⠀⠀⠰⠁⠀⡎⠀⡰⠑⠢⡸⣏⡾⠁
        ⠀⠀⡆⠀⠎⠸⣀⠀⠀⠀⠀⠀⠢⢄⠀⡁⠜⣉⠠⠚⡄⠀⠀⠈⠉⠀⠀
        ⠀⢰⠁⡘⠀⡏⠀⠈⠉⠁⠀⠀⢒⠒⠋⠈⠉⢀⠠⡊⠀⠀⠀⠀⠀⠀⠀
        ⠀⠸⢠⠁⢠⠁⠀⠉⠁⠀⠒⠒⠋⠐⠂⠀⠉⠀⠀⠓⠄⡀⠀⠀⠀⠀⠀
        ⠀⢸⠈⡔⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⠄⠀⠀⠀
        ⠀⢸⢼⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡄⠀⠀
        ⠀⠘⢬⣄⡀⠀⠀⠀⠀⠀⢀⠮⠓⠂⠄⣑⠂⠤⠀⠀⠀⠀⠠⢴⠃⠀⠀
        ⠀⠀⠀⠑⠠⠥⠤⠤⠤⠭⠚⠁⠀⠀⠀⠀⠈⠉⠁⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
            """
            print(gnome)

            print(
                f"    |    A random gnome has appeared and cast a spell!  You hear it run and laugh as you start seeing double.")
            # If hero's health is already 1, do not make a change
            if health_points == 1:
                print(f"Your health is already dangerously low.  Be careful!")
            else:
                # If hero's health is above 1, ensure the lowest hero health can fall to is 1
                print(f"    |    Your {stat} went down from {health_points} to {max(1, health_points // 2)}"
                      f" and {combat_strength} to {max(1, combat_strength // 2)}!")
                health_points = max(1, health_points // 2)
                combat_strength = max(1, combat_strength // 2)
            print(f"    |    Suspiciously, the monster is unaffected...")
    else:
        if weather["affected"] == "hero" and weather["effect"] == "up":
            print(f"    |    The {weather["term"]} seems to be energizing you...  Your {stat} have increased.")
            print(f"    |    Your {stat} went up from {health_points} to {health_points + h_modifier}!")
            health_points += h_modifier
        elif weather["affected"] == "hero" and weather["effect"] == "down":
            print(f"    |    The {weather["term"]} is making you feel uneasy...  Your {stat} have decreased.")
            # If hero health is already 1, do not make a change
            if health_points == 1:
                print("Your health is already dangerously low.  Be careful!")
            else:
                # If hero's health is above 1, ensure the lowest hero health can fall to is 1
                print(f"    |    Your {stat} went down from {health_points} to {max(1, (health_points - h_modifier))}!")
                health_points = max(1, (health_points - h_modifier))
        elif weather["affected"] == "monster" and weather["effect"] == "up":
            print(f"    |    The monster appears to be enjoying the {weather["term"]}.  Its {stat} have increased.")
            print(f"    |    The monster's {stat} went up from {m_health_points} to {m_health_points + m_modifier}!")
            m_health_points += m_modifier
        elif weather["affected"] == "monster" and weather["effect"] == "down":
            print(f"    |    The monster appears to be reacting to the {weather["term"]}.  Its {stat} have decreased.")
            # If monster's health is already 1, do not make a change
            if m_health_points == 1:
                print(f"    |    The monster's health is already at its lowest.  The odds are in your favour!")
            else:
                # If monster's health is above 1, ensure the lowest monster health can fall to is 1
                print(
                    f"    |    The monster's {stat} went down from {m_health_points} to {max(1, (m_health_points - m_modifier))}!")
                m_health_points = max(1, (m_health_points - m_modifier))
        elif weather["affected"] == "none":
            print("    |    Nothing seems to have happened...")

    # ---------------------------NEZ: LEVEL UP-------------------------------------------
    # ---------------------------PENNY: CRAZY SCIENTIST----------------------------------

    # Crazy Scientist Feature
    print("    ------------------------------------------------------------------")
    print("    |    The Hero comes across a door that leads into a Science Lab")
    input("    |    Is the door unlocked? Roll the dice to find out! (Press enter)")
    door_roll = random.choice(big_dice_options)
    door_unlocked = False
    mood = "bad_mood"

    if door_roll in range (1, 17):
        door_unlocked = True
        print("    |    The door is unlocked")
        print("    |    You go inside to see a Scientist working")
        input("    |    Roll the dice to find out if the Scientist is in a good or bad mood. (Press enter)")

        mood_roll = random.choice(small_dice_options)
        print("    |    ")

        if mood_roll % 2 == 0:
            mood = "good_mood"
            print("    |    Great news, the Scientist is in a good mood today and will attempt an experiment "
                  "to help you fight the monster.")
        elif mood_roll % 2 == 1:
            mood = "bad_mood"
            print("    |    Oh no, the Scientist is angry to have been disturbed!")
            print("    |    Now they are in a bad mood and will attempt an experiment to help the monster!")

        # This code should only execute if the door is unlocked
        # Define the possible outcomes of the cloning experiment
        cloning_experiments_and_outcomes = {
            'good_mood': ['The hero have been successfully cloned!',
                          'The attempt to clone the hero failed!',
                          'The hero has been cloned, but it was a very strenuous and the hero is now weakened.'
                          ],
            'bad_mood': ['Oh no! The monster has been successfully cloned!',
                         'What a relief, the attempt to clone the monster failed!',
                         'Plot twist! The monster clone joins the hero to fight the original monster.'
                         ]
        }

        # The possible cloning outcomes is based on mood
        possible_cloning_outcomes = [outcome for key, outcomes in cloning_experiments_and_outcomes.items()
                                     if key == mood for outcome in outcomes]

        print(f"    |    The possible cloning outcomes are: {possible_cloning_outcomes}")
        input(
            "    |    Continue to find out what happens when the Scientist attempts their experiment. (Press enter)")

        # Roll the dice to select one of the possible cloning outcomes
        outcome_roll = random.choice(possible_cloning_outcomes)
        print("    |    The outcome of the experiment is:")
        print(f"    |    {outcome_roll}")
        if outcome_roll == 'The hero have been successfully cloned!':
            print("    |    As a result the Hero's Combat Strength and Health Points have doubled.")
            health_points *= 2
            combat_strength *= 2
        elif outcome_roll == 'The attempt to clone the hero failed!':
            print("    |    No change is made to the Hero's Combat Strength and Health Points.")
        elif outcome_roll == 'The hero has been cloned, but it was a very strenuous and the hero is now weakened.':
            print("    |    The Hero's Combat Strength is reduced to half but the Health Points have doubled.")
            health_points *= 2
            combat_strength //= 2
        elif outcome_roll == 'Oh no! The monster has been successfully cloned!':
            print("    |    As a result the Monster's Combat Strength and Health Points have doubled.")
            m_health_points *= 2
            m_combat_strength *= 2
        elif outcome_roll == 'What a relief, the attempt to clone the monster failed!':
            print("    |    No change is made to the Monster's Combat Strength and Health Points.")
        elif outcome_roll == 'Plot twist! The monster clone joins the hero to fight the original monster.':
            print("    |    As a result the Monster's Combat Strength and Health Points have been reduced to half.")
            m_health_points //= 2
            m_combat_strength //= 2
        print("    |    You escape from the Science Lab before something even crazier happens!")
    else:
        print("    |    The door is locked and you cannot enter.")

    # Print out the updated combat strength and health points for the Hero and Monster
    print("")
    print("    |    The Hero and Monster Combat Strength and Health Points are set as follows:")
    print(f"Hero's Health Points: {health_points}")
    print(f"Hero's Combat Strength: {combat_strength}")
    print(f"Monster's Health Points: {m_health_points}")
    print(f"Monster's Combat Strength: {m_combat_strength}")
    print("")
    print("    ------------------------------------------------------------------")

    # ---------------------------JAMES: DRAGON'S DEN-------------------------------------

    print("The hero has selected these dragons from the Dragon's Den:", [dragon['name'] for dragon in hero_dragons])

    # Fight Sequence
    # Loop while the monster and the player are alive. Call fight sequence functions
    print("    ------------------------------------------------------------------")
    print("    |    You meet the monster. FIGHT!!")

    wizard_protection = False

    while m_health_points > 0 and health_points > 0:

        # Check to see if the wizard appears to assist the hero
        if health_points <= 6:
            print("     |     A wizard appears in a burst of magical energy!")

            if health_points % 2 == 0:  # Even number health points: Grant temporary invincibility
                print("     |     The wizard casts a spell...You are invincible for one attack!")
                wizard_protection = True  # Set protection flag

            else:  # Odd number health points: Gain 10 health points
                print("     |     The wizard waves his staff...The spell heals you by 10 health points!")
                health_points += 10
                print("     |     Your new health is: " + str(health_points) + "HP")


        # Fight Sequence
        print("    |", end="    ")

        # Determine who goes first
        input("Roll to see who strikes first (Press Enter)")
        attack_roll = random.choice(small_dice_options)

        if attack_roll % 2 != 0:  #Hero attacks first
            print("    |", end="    ")
            input("You strike(Press enter)")

            # Check if a dragon enters the battle (Shield or Attack)
            for dragon in hero_dragons:
                # if health_points < 5 and dragon ["role"] == "Shield":
                if health_points < 10 and health_points % 2 == 0 and dragon["role"] == "Shield":
                    print(f" {dragon['name']} will shield you from the monster's attack!")
                    print(f"     |  {dragon['name']} shields you from damage!")
                    health_points += 10
                    print("health points: " + str(health_points))
                    break  # Stop after the first Shield dragon acts

                elif 10 < health_points < 20 and health_points % 2 != 0 and dragon["role"] == "Attack":
                    print(f" {dragon['name']} joins the attack!")
                    print(f"     |  {dragon['name']} attacks causing damage!")
                    m_health_points -= 5
                    print("monster health points: " + str(m_health_points))
                    break  # Stop after the first Attack dragon acts

                else:
                    # This handles the case where the dragon neither shields nor attacks
                    print(f"The monster strikes fear in {dragon['name']} who does not act this turn.")

            # Hero attacks the monster
            m_health_points = functions.hero_attacks(combat_strength, m_health_points)

            if m_health_points == 0:
                num_stars = 3
            else:
                print("    |", end="    ")
                print("--------------------------------------------------")
                input("     |     The monster strikes (Press enter)!!!")

                # Monster attacks hero
                if wizard_protection:
                    print("     |     The wizard’s magic shields you! No damage taken.")
                    wizard_protection = False  # Remove protection after one attack
                else:
                    health_points = functions.monster_attacks(m_combat_strength, health_points)

                if health_points == 0:
                    num_stars = 1
                else:
                    num_stars = 2

        else:  # Monster attacks first
            print("    |", end="    ")
            input("The monster strikes (Press enter)")

            # Check if a dragon should shield the hero
            for dragon in hero_dragons:
                if health_points < 10 and health_points % 2 == 0 and dragon["role"] == "Shield":
                    print(f" {dragon['name']} will shield you from the monster's attack!")
                    print(f"     |  {dragon['name']} shields you from damage!")
                    health_points += 10
                    print("health points: " + str(health_points))
                    break  # Stop after the first Shield dragon acts

                elif 10 < health_points < 20 and health_points % 2 != 0 and dragon["role"] == "Attack":
                    print(f" {dragon['name']} joins the attack!")
                    print(f"     |  {dragon['name']} attacks causing damage!")
                    m_health_points -= 5
                    print("monster health points: " + str(m_health_points))
                    break  # Stop after the first Attack dragon acts

                else:
                    # This handles the case where the dragon neither shields nor attacks
                    print(f"The monster strikes fear in {dragon['name']} who does not act this turn.")


            # Monster attacks the hero
            if wizard_protection:
                print("     |     The wizard’s magic shields you! No damage taken.")
                wizard_protection = False  # Remove protection after one attack
            else:
                health_points = functions.monster_attacks(m_combat_strength, health_points)

            if health_points == 0:
                num_stars = 1
            else:
                print("    |", end="    ")
                print("----------------------------------------------------")
                input("The hero strikes (Press enter)")

                # Hero attacks the monster
                m_health_points = functions.hero_attacks(combat_strength, m_health_points)

                if m_health_points == 0:
                    num_stars = 3
                else:
                    num_stars = 2

    # Determine the winner
    if (m_health_points <= 0):
        winner = "Hero"
    else:
        winner = "Monster"

    # Final Score Display
    tries = 0
    input_invalid = True
    while input_invalid and tries in range(5):
        print("    |", end="    ")

        hero_name = input("Enter your Hero's name (in two words)")
        name = hero_name.split()
        if len(name) != 2:
            print("    |    Please enter a name with two parts (separated by a space)")
            tries += 1
        else:
            if not name[0].isalpha() or not name[1].isalpha():
                print("    |    Please enter an alphabetical name")
                tries += 1
            else:
                short_name = name[0][0:2:1] + name[1][0:1:1]
                print("    |    I'm going to call you " + short_name + " for short")
                input_invalid = False

    if not input_invalid:
        stars_display = "*" * num_stars
        print("    |    Hero " + short_name + " gets <" + stars_display + "> stars")

        functions.save_game(winner, hero_name=short_name, num_stars=num_stars)


