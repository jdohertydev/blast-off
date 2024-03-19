#Import the random module

import random

def initiate_game():
    """
    Initiates the game.

    """

    print("Welcome to 'Blast Off'!\n")
    print("You have been selected for a very special mission. Before we tell you more...\n")

def validate_name(): 
    """
    Ensures user enters a valid name.

    """
    
    while True:
        name = input("What is your name? ")
        try:
            int(name)
            print(f"{name} isn't a name on our VIP list, try again.")            
            
        except ValueError:
            print(f"\nThanks, Commander {name}. One more thing. To make sure you are ready for your mission, we have one more question...\n")
            return name            

def validate_plants(name):
    """
    Validates user's answer is a number.
    
    """

    plant_number = int(input("How many planets are there in our Solar System? "))

    if plant_number == 9 or plant_number == "nine" or plant_number == "Nine":
        print(f"\nWell done! You know your stuff, Commander {name}. It's time to commence the mission!")
    else:
        print(f"Hmm, {plant_number} isn't quite right, Commander {name}. Try again.")

 
initiate_game()
name = validate_name()
validate_plants(name)