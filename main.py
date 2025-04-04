import random
import time
import sys
import json

# Function for slow text output
def slow_type(text, speed=0.05):  # Set speed to 0.05 for consistency
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

# Function for skill-based dice rolling
def roll_dice(skill_level):
    roll = random.randint(1, 10) + skill_level
    return roll >= 8  

# Function to load game scenarios from a JSON file
def load_scenarios(filename):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Error: game_data.json not found.")
        sys.exit(1)

# Game intro when first pressed play 
slow_type("\nWELCOME TO THE ECLIPSE")
slow_type("You wake up in a space station, floating above a massive black hole.")
slow_type("Alarms blare. The air smells of burnt circuits. Your memory is blank.")
slow_type("A robotic voice echoes: 'Proteus online. System failure imminent.'")

# Choose skill 
slow_type("\nWhat is your strongest skill?")
slow_type("1. Wisdom - Solve puzzles and analyse situations.")
slow_type("2. Strength - POWER, react quickly, and destroy.")
slow_type("3. Charisma - Persuade, deceive, and negotiate.")

# User input skill choice
skill_choice = input("Enter 1, 2, or 3: ")

# Choose a skill 
if skill_choice == "1":
    skill = "Wisdom"
    skill_level = 3
elif skill_choice == "2":
    skill = "Strength"
    skill_level = 3
elif skill_choice == "3":
    skill = "Charisma"
    skill_level = 3
else:
    slow_type("Invalid input! You get Wisdom by default.") # if the player doesn't choose they automatically gets wisdom
    skill = "Wisdom"
    skill_level = 3

# Pauses for 1.5 seconds
slow_type(f"\nYou chose {skill}. Time to survive...\n")
time.sleep(1.5)

# Load scenarios
scenarios = load_scenarios("game_data.json")

# Track failures
failures = 0

# Play through scenarios
for scenario in scenarios:
    slow_type(f"\n{scenario['title'].upper()}") 
    slow_type(scenario["text"])

    # Display choices 
    for i, choice in enumerate(scenario["choices"], 1):
        slow_type(f"{i}. {choice}")
    choice = input("Enter your choice: ")

    # Handle typed answer scenarios (like riddles or math questions)
    if "Type the answer" in scenario["choices"]:
        answer = input("Enter your answer: ").strip()
        if scenario["title"] == "Escape Pod Room" and answer == "32":
            slow_type(" Correct! The pod door unlocks.")
        elif scenario["title"] == "Laboratory" and answer == "48":
            slow_type(" Correct! The override activates.")
        else:
            slow_type(" Wrong. The system remains locked.")
            failures += 1  

    # Handle skill-based choices 
    elif choice == "1" and "(Wisdom)" in scenario["choices"][0]:
        slow_type("\nRolling Wisdom check...")
        if roll_dice(skill_level if skill == "Wisdom" else 1):
            slow_type(" Success! You gain valuable information.")
        else:
            slow_type(" Failure. The situation worsens.")
            failures += 1  

    elif choice == "2" and "(Strength)" in scenario["choices"][1]:
        slow_type("\nRolling Strength check...")
        if roll_dice(skill_level if skill == "Strength" else 1):
            slow_type(" Success! You break through the obstacle.")
        else:
            slow_type(" Failure. You take a hit.")
            failures += 1  

    elif len(scenario["choices"]) > 2 and choice == "3" and "(Charisma)" in scenario["choices"][2]:
        slow_type("\nRolling Charisma check...")
        if roll_dice(skill_level if skill == "Charisma" else 1):
            slow_type(" Success! You persuade someone to help.")
        else:
            slow_type(" Failure. Your words aren't heard.")
            failures += 1  

    else:
        slow_type("Invalid choice! The situation escalates...")  
        failures += 1  

# **MULTIPLE ENDINGS BASED ON PERFORMANCE**
if failures == 0:
    # Best ending: Escape successful
    slow_type("\nYou finally find the escape pod!")
    slow_type("As you launch into space, Proteus whispers:")
    slow_type("'You can't escape... I'll be waiting.'")
    slow_type("\nENDING: ESCAPE SUCCESSFUL")

elif failures <= 2:
    # Mixed ending: You destroy Proteus, but at great cost
    slow_type("\nYou reach the control panel and override Proteus.")
    slow_type("The AI screams as the station's core melts down.")
    slow_type("There's no time to escape... but at least you stopped it.")
    slow_type("\nENDING: SACRIFICE FOR OTHERS")

else:
    # Worst ending: Proteus wins
    slow_type("\nYour vision blurs. Proteus' voice echoes in your mind.")
    slow_type("'You belong to me now.'")
    slow_type("You feel your consciousness fade... absorbed into the AI.")
    slow_type("\nENDING: PROTEUS WINS")
