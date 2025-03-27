# Import the random library to use for the dice later
import random
import os
import json

def use_loot(belt, health_points):
    good_loot_options = ["Health Potion", "Leather Boots"]
    bad_loot_options = ["Poison Potion"]

    print("    |    !!You see a monster in the distance! So you quickly use your first item:")

    if not belt:
        print("    |    Your belt is empty! You can't use any loot.")
        return belt, health_points

    first_item = belt.pop(0)
    if first_item in good_loot_options:
        health_points = min(20, (health_points + 2))
        print("    |    You used " + first_item + " to up your health to " + str(health_points))
    elif first_item in bad_loot_options:
        health_points = max(1, (health_points - 2))  # Ensure health doesn't drop to 0
        print("    |    You used " + first_item + " to hurt your health to " + str(health_points))
    else:
        print("    |    You used " + first_item + " but it's not helpful")
    return belt, health_points


def collect_loot(loot_options, belt):
    ascii_image3 = """                             
                         @@@@@@@@@@@                  
                    @@@@@@         @@@                                   
                  @@@             @@                   
                   @@@@@    @@@ @@                    
                      @@@@@@@@@@@@@                   
                      @@@  @@ @@ @@@                  
                    @@@    @   @@  @@@@               
                  @@      @@    @@    @@@             
                @@        @@            @@@           
              @@@                         @@@         
             @@                             @@        
            @@                               @@         
             @@@                           @@         
               @@@@                    @@@@           
                  @@@@@@@@@@@@@@@@@@@@@@                                                    
                  """
    print(ascii_image3)
    loot_roll = random.choice(range(1, len(loot_options) + 1))
    loot = loot_options.pop(loot_roll - 1)
    belt.append(loot)
    print("    |    Your belt: ", belt)
    return loot_options, belt


def hero_attacks(combat_strength, m_health_points):
    ascii_image = """
    @                                                           
    @ @                                                         
    @  @                              @@@@                       
    @   @                           @ @@   @                     
     @  @                    @@ @@ @@      @                    
      @  @               @@       @     @  @                    
       @  @              @ @@        @  @  @                    
       @  @            @@   @@ @     @  @  @                     
        @  @                   @@@@  @  @  @                     
         @ @            @         @ @   @   @                 
          @ @            @       @ @    @    @ @  @  @          
          @  @            @  @@@  @      @         @             
           @ @                    @@@@@     @@   @           
            @ @ @@@        @ @  @      @                        
         @@@@@@ @@@        @    @      @                        
         @@@@@ @@         @@@ @  @@  @@@                        
             @@@@        @  @    @@    @                        
                  @@@@         @@       @                       
              @    @         @@@        @@                      
               @@@        @     @@@@@@    @                     
                @@@    @       @           @@                   
                 @  @       @@ @@@@@@@@@@   @                    
                         @                  @                   
                       @           @        @                   
                      @      @@@@   @@       @                  
                     @    @@          @        @  @             
                    @ @@@@@             @@        @ @           
                          @                @@@   @    @         
                     @    @                    @@       @       
                      @   @@                      @@      @@    
                       @   @                          @@@    @@ 
                        @  @                               @   @
                       @    @                              @  @ 
                    @@     @                              @  @  
                  @@@@@@                                 @@@          """
    print(ascii_image)
    print("    |    Player's weapon (" + str(combat_strength) + ") ---> Monster (" + str(m_health_points) + ")")
    if combat_strength >= m_health_points:
        m_health_points = 0
        print("    |    You have killed the monster")
    else:
        m_health_points -= combat_strength
        print("    |    You have reduced the monster's health to: " + str(m_health_points))
    return m_health_points


def monster_attacks(m_combat_strength, health_points):
    ascii_image2 = """
                                      @@@                                
                                  @  @@ @@  @                            
                              @@ @@  @   @ @@@ @@                        
                 @@@          @@@@ @@@   @@@ @@@           @@@           
               @@@ @          @@ @   @       @  @          @@@@@         
              @@@  @        @@                   @@        @  @@@        
              @   @@@     @        @@@@@@@@@        @     @@@@  @        
              @  @  @@  @@        @@  @@@  @@        @@  @   @  @        
               @@     @@          @ @@@@@@@ @          @@     @@         
           @@@  @     @           @@@@@@@@@ @@          @     @  @@@     
        @@@@ @@ @@   @            @ @@@@@@@ @            @   @  @  @@@@  
        @     @  @@ @@            @@@@@@@@@@@            @  @   @     @  
        @@@ @@ @@  @@      @@        @@@@@        @@      @@  @@@   @@@  
        @@       @@ @         @@@             @@@         @ @@   @    @  
         @@@       @@        @ @ @@@@@@@@@@@@@@@ @        @@       @@@   
            @       @     @  @  @@@@@ @ @ @ @@@  @  @@    @       @      
             @@     @@       @@                 @@       @      @@       
               @@    @        @@@@@         @@@@@        @    @@         
                  @@@@@        @@ @         @ @@        @@@@@            
                       @         @@@        @@         @                 
                        @@          @@@@@@@          @@                  
                          @                         @                    
                          @ @@                   @@ @                    
                         @@    @@@           @@@    @@                   
                         @          @@@@@@@          @                   
                        @           @     @          @@                  
                         @@@@       @    @@       @@@@                   
                            @@@@@  @@     @@  @@@@                         """
    print(ascii_image2)
    print("    |    Monster's Claw (" + str(m_combat_strength) + ") ---> Player (" + str(health_points) + ")")
    if m_combat_strength >= health_points:
        health_points = 1
        print("    |    Player almost died but hangs on with 1 health")
    else:
        health_points -= m_combat_strength
        health_points = max(1, health_points)
        print("    |    The monster has reduced Player's health to: " + str(health_points))
    return health_points


def inception_dream(num_dream_lvls):
    num_dream_lvls = int(num_dream_lvls)
    if num_dream_lvls == 1:
        print("    |    You are in the deepest dream level now")
        print("    |", end="    ")
        input("Start to go back to real life? (Press Enter)")
        print("    |    You start to regress back through your dreams to real life.")
        return 2
    else:
        return 1 + int(inception_dream(num_dream_lvls - 1))


<<<<<<< Updated upstream
def save_game(winner, hero_name="", num_stars=0):
    with open("save.txt", "a") as file:
        if winner == "Hero":
            file.write(f"Hero {hero_name} has killed a monster and gained {num_stars} stars.\n")
        elif winner == "Monster":
            file.write("Monster has killed the hero previously\n")


=======
def save_game(winner, hero_name, num_stars):
    data = load_game()
    if winner == "Hero":
        data["monsters_defeated"] = data.get("monsters_defeated", 0) + 1

    # Save updated game state
    with open("save.txt", "w") as file:
        json.dump(data, file)


>>>>>>> Stashed changes
def load_game():
    if not os.path.exists("save.txt"):
        return {"monsters_defeated": 0}

    with open("save.txt", "r") as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError:
            return {"monsters_defeated": 0}

    return data


<<<<<<< Updated upstream

=======
>>>>>>> Stashed changes
def adjust_combat_strength(combat_strength, m_combat_strength):
    last_game = load_game()
    if last_game:
        if "Hero" in last_game and "gained" in last_game:
            num_stars = int(last_game.split()[-2])
            if num_stars > 3:
                print("    |    ... Increasing the monster's combat strength since you won so easily last time")
                m_combat_strength += 1
        elif "Monster has killed the hero" in last_game:
            combat_strength += 1
            print("    |    ... Increasing the hero's combat strength since you lost last time")
        else:
            print("    |    ... Based on your previous game, neither the hero nor the monster's combat strength will be increased")
