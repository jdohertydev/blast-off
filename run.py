#Import the random module

import random

def initiate_game():
    """
    Initiates the game.
    Ensures user enters a valid name and answers a basic question before main game starts.

    """

    print("Welcome to 'Blast Off'!\n")
    print("You have been selected for a very special mission. Before we tell you more...\n")
    
    while True:

        name = input("What is your name? ")

        try:
            int(name)
            print(f"{name} isn't a name on our list, try again")            
        
        except ValueError:
            print(f"\nThanks, Commander {name}. One more thing. To make sure you are ready for your mission, we have one more question...\n")
            break

    plant_number = int(input("How many planets are there in our Solar System? "))
    
    if plant_number == 9:
        print("\nWell done! You know your stuff, Commander {name}. It's time to commence the mission")
    else:
        print(f"Hmm, {plant_number} isn't quite right, Commander {name}.")

initiate_game()