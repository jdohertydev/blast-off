#Import the random module

import random
import time,sys
import os

def typing_print(text):
    """
    https://www.101computing.net/python-typing-text-effect/
    """
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
  
def typing_input(text):
    """
    https://www.101computing.net/python-typing-text-effect/

    """
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    value = input()  
    return value

def clear_screen():
    """
    https://www.101computing.net/python-typing-text-effect/

    """
    os.system("clear")

def initiate_game():
    """
    Initiates the game.

    """
    typing_print("Welcome to 'Blast Off'!\n")
    typing_print("You have been selected for a very special mission. Before we tell you more...\n")

def validate_name(): 
    """
    Ensures user enters a valid name.

    """
    while True:
        name = typing_input("What is your name? ")

        try:
            int(name)
            typing_print(f"{name} isn't a name on our VIP list, try again using letters from the alpabet.")            
            
        except ValueError:
            name = name.capitalize()
            typing_print(f"\nThanks, Commander {name}. One more thing. To make sure you are ready for your mission, we have one more question...\n")
            return name            

def validate_plants(name):
    """
    Validates user's answer is a digit.
    
    """
    while True:
        try:
            plant_number = int(typing_input("How many planets are there in our Solar System? "))

            if plant_number == 9:
                typing_print(f"\nWell done! You know your stuff, Commander {name}. It's time to commence the mission!")
                break
            else:
                typing_print(f"Hmm, {plant_number} isn't quite right, Commander {name}. Try again.")
        except ValueError:
            typing_print(f"Please enter a number as a digit, e.g. 1, Commander {name}.")  
 
initiate_game()
name = validate_name()
validate_plants(name)