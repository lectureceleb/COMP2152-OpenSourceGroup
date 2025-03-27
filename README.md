
## Nezihe Tekin – Level-Up Feature

 **Level-Up ** based on the hero's past game performance.

### Purpose
To dynamically adjust the monster's difficulty level based on how many monsters the hero has defeated in previous games.

### How It Works
- The game reads the last saved result using `load_game()`.
- Based on the number of monsters defeated, the hero’s level is calculated:
  - `Level = total_monsters_killed // 3`
- Depending on the hero's level, the upcoming monster becomes:
  -  **Elite Monster** (Level ≥ 3): +10 HP, +2 Combat Strength
  -  **Stronger Monster** (Level 1–2): +5 HP, +1 Combat Strength
  -  **Regular Monster** (Level 0): No changes

### Data Handling
- Game progress is read from the `save.txt` file.
- Monster difficulty is scaled **before** the battle begins.

### Benefits
- Adds replay value by increasing difficulty as the player improves.
- Simple logic that integrates seamlessly with the main game flow.
