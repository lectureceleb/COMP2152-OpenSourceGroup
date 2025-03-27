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

    if (not combat_strength.isnumeric()) or (not m_combat_strength.isnumeric()):
        print("    |    One or more invalid inputs. Player needs to enter integer numbers for Combat Strength    |")
        i += 1
        continue
    elif (int(combat_strength) not in range(1, 7)) or (int(m_combat_strength) not in range(1, 7)):
        print("    |    Enter a valid integer between 1 and 6 only")
        i += 1
        continue
    else:
        input_invalid = False
        break

if not input_invalid:
    combat_strength = int(combat_strength)
    m_combat_strength = int(m_combat_strength)

    print("    |", end="    ")
    input("Roll the dice for your weapon (Press enter)")
    weapon_roll = random.choice(small_dice_options)
    combat_strength = min(6, (combat_strength + weapon_roll))
    print("    |    The hero's weapon is " + str(weapons[weapon_roll - 1]))
    functions.adjust_combat_strength(combat_strength, m_combat_strength)

    print("    ------------------------------------------------------------------")
    print("    |", end="    ")
    input("Analyze the Weapon roll (Press enter)")
    if weapon_roll <= 2:
        print("--- You rolled a weak weapon, friend")
    elif weapon_roll <= 4:
        print("--- Your weapon is meh")
    else:
        print("--- Nice weapon, friend!")

    if weapons[weapon_roll - 1] != "Fist":
        print("    |    --- Thank goodness you didn't roll the Fist...")

    print("    |", end="    ")
    input("Roll the dice for your health points (Press enter)")
    health_points = random.choice(big_dice_options)
    print("    |    Player rolled " + str(health_points) + " health points")

    print("    |", end="    ")
    input("Roll the dice for the monster's health points (Press enter)")
    m_health_points = random.choice(big_dice_options)
    print("    |    Player rolled " + str(m_health_points) + " health points for the monster")

    print("    ------------------------------------------------------------------")
    print("    |    !!You find a loot bag!! You look inside to find 2 items:")
    print("    |", end="    ")
    input("Roll for first item (enter)")
    loot_options, belt = functions.collect_loot(loot_options, belt)
    print("    ------------------------------------------------------------------")
    print("    |", end="    ")
    input("Roll for second item (Press enter)")
    loot_options, belt = functions.collect_loot(loot_options, belt)
    belt.sort()
    print("    |    Your belt: ", belt)

    belt, health_points = functions.use_loot(belt, health_points)
    health_points = max(1, health_points)

    print("    ------------------------------------------------------------------")
    print("    |", end="    ")
    input("Analyze the roll (Press enter)")
    print("    |    --- You are matched in strength: " + str(combat_strength == m_combat_strength))
    print("    |    --- You have a strong player: " + str((combat_strength + health_points) >= 15))

    print("    |", end="    ")
    input("Roll for Monster's Magic Power (Press enter)")
    power_roll = random.choice(["Fire Magic", "Freeze Time", "Super Hearing"])
    m_combat_strength += min(6, m_combat_strength + monster_powers[power_roll])
    print("    |    The monster's combat strength is now " + str(m_combat_strength) + " using the " + power_roll + " magic power")

    num_dream_lvls = -1
    while num_dream_lvls < 0 or num_dream_lvls > 3:
        print("    |", end="    ")
        num_dream_lvls = input("How many dream levels do you want to go down? (Enter a number 0-3)")
        if num_dream_lvls == "":
            num_dream_lvls = -1
            print("Number entered must be a whole number between 0-3 inclusive, try again")
        else:
            num_dream_lvls = int(num_dream_lvls)
            if num_dream_lvls < 0 or num_dream_lvls > 3:
                num_dream_lvls = -1
                print("Number entered must be a whole number between 0-3 inclusive, try again")
            elif num_dream_lvls != 0:
                health_points -= 1
                health_points = max(1, health_points)
                crazy_level = functions.inception_dream(num_dream_lvls)
                combat_strength += crazy_level
                print("combat strength: " + str(combat_strength))
                print("health points: " + str(health_points))
        print("num_dream_lvls: ", num_dream_lvls)

    # ---------------------------OMAR: WEATHER EFFECTS-----------------------------------
    # ---------------------------NEZIHE: LEVEL UP-------------------------------------------

    # Load previous game state to determine level-up
    print("    |    Loading from saved file ...")
    game_result = functions.load_game()
    monsters_killed = 0

    if game_result and "Hero" in game_result:
        try:
            print(game_result)
            monsters_killed = sum([int(line.split("gained")[1].strip().split()[0]) for line in open("save.txt") if "gained" in line])
        except (IndexError, ValueError):
            monsters_killed = 0

    hero_level = monsters_killed // 3
    print("    |    Based on your game history, your hero level is:", hero_level)

    if hero_level >= 3:
        print("    |    You are facing an ELITE monster due to your level.")
        m_health_points += 10
        m_combat_strength = min(6, m_combat_strength + 2)
    elif hero_level >= 1:
        print("    |    You are facing a STRONGER monster due to your level.")
        m_health_points += 5
        m_combat_strength = min(6, m_combat_strength + 1)
    else:
        print("    |    You are facing a REGULAR monster.")

    # ---------------- Safe Type Enforcement ----------------
    health_points = max(1, int(health_points))
    combat_strength = max(1, int(combat_strength))
    m_health_points = max(1, int(m_health_points))
    m_combat_strength = max(1, int(m_combat_strength))

    # Fight Loop
    print("    ------------------------------------------------------------------")
    print("    |    You meet the monster. FIGHT!!")
    while m_health_points > 0 and health_points > 0:
        print("    |", end="    ")
        input("Roll to see who strikes first (Press Enter)")
        attack_roll = random.choice(small_dice_options)

        if not (attack_roll % 2 == 0):
            print("    |", end="    ")
            input("You strike (Press enter)")
            m_health_points = functions.hero_attacks(combat_strength, m_health_points)
            if m_health_points == 0:
                num_stars = 3
            else:
                print("    |", end="    ")
                print("------------------------------------------------------------------")
                input("    |    The monster strikes (Press enter)!!!")
                health_points = functions.monster_attacks(m_combat_strength, health_points)
                if health_points == 0:
                    num_stars = 1
                else:
                    num_stars = 2
        else:
            print("    |", end="    ")
            input("The Monster strikes (Press enter)")
            health_points = functions.monster_attacks(m_combat_strength, health_points)
            if health_points == 0:
                num_stars = 1
            else:
                print("    |", end="    ")
                print("------------------------------------------------------------------")
                input("The hero strikes!! (Press enter)")
                m_health_points = functions.hero_attacks(combat_strength, m_health_points)
                if m_health_points == 0:
                    num_stars = 3
                else:
                    num_stars = 2

    winner = "Hero" if m_health_points <= 0 else "Monster"

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
