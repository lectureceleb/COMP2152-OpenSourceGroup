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
    num_dream_lvls = -1 # Initialize the number of dream levels
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

    # ---------------------------OMAR: WEATHER EFFECTS-----------------------------------
    # ---------------------------NEZ: LEVEL UP-------------------------------------------
    # ---------------------------PENNY: CRAZY SCIENTIST----------------------------------
    # ---------------------------JAMES: DRAGON'S DEN-------------------------------------

    print("DEBUG: Selected hero dragons:", [dragon['name'] for dragon in hero_dragons])

    # Fight Sequence
    # Loop while the monster and the player are alive. Call fight sequence functions
    print("    ------------------------------------------------------------------")
    print("    |    You meet the monster. FIGHT!!")
    while m_health_points > 0 and health_points > 0:
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
                if health_points < 15 and dragon ["role"] == "Shield":
                # if health_points < 10 and health_points % 2 == 0 and dragon["role"] == "Shield":
                    print(f"     |  {dragon['name']} shields you from damage!")
                elif dragon ["role"] == "Attack":
                # elif 10 < health_points < 20 and health_points % 2 != 0 and dragon["role"] == "Shield":
                #    print(f"     |  {dragon['name']} shields you from damage!")
                # elif dragon["role"] == "Attack":
                    print(f"DEBUG: {dragon['name']} is attacking!")
                    print(f"     |  {dragon['name']} joins the attack!")
                    m_health_points -= 13

            # Hero attacks the monster
            m_health_points = functions.hero_attacks(combat_strength, m_health_points)

            if m_health_points == 0:
                num_stars = 3
            else:
                print("    |", end="    ")
                print("--------------------------------------------------")
                input("     |     The monster strikes (Press enter)!!!")

                # Monster attacks hero
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
                    print(f"     |  {dragon['name']} shields you from damage!")
                elif 10 < health_points < 20 and health_points % 2 != 0 and dragon["role"] == "Shield":
                    print(f"     |  {dragon['name']} shields you from damage!")


            # Monster attacks the hero
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
    if m_health_points <= 0:
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


