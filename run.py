#Import the random module

import random
import time,sys
import os

import constants
# from constants import word_list

def typing_print(text):
    """
    https://www.101computing.net/python-typing-text-effect/

    Creates a typing effect to improve user experience.

    """
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
  
def typing_input(text):
    """
    https://www.101computing.net/python-typing-text-effect/

    Creates a typing effect to improve user experience.

    """
    typing_print(text)
    value = input()  
    return value

def clear_screen():
    """
    https://www.101computing.net/python-typing-text-effect/

    Clears user's screen improve user experience.

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
    Validates that the user enters a name.

    """
    while True:
        name = typing_input("What is your name? ")
        
        if not name.strip():  # Check if the input is empty or contains only whitespace
            typing_print("We need a valid name, Commander. ")
            continue
        try:
            int(name)
            typing_print(f"{name} isn't a name on our VIP list, try again using letters from the alpabet.")            
            
        except ValueError:
            name = name.capitalize()
            typing_print(f"\nThanks, Commander {name}. One more thing. To make sure you are ready for your mission, we have one more question...\n")
            return name            

def validate_plants(name):
    """
    Validates that the answer is a digit.
    
    """
    while True:
        try:
            plant_number = int(typing_input("How many planets are there in our Solar System? "))

            if plant_number == 9:
                typing_print(f"\nWell done! You know your stuff, Commander {name}. Your mission will commence in 5...")
                time.sleep(1)
                typing_print("4...")
                time.sleep(1)
                typing_print("3...")
                time.sleep(1)
                typing_print("2...")
                time.sleep(1)
                typing_print("1...")
                time.sleep(1)
                clear_screen()
                break
            else:
                typing_print(f"Hmm, {plant_number} isn't quite right, Commander {name}. Try again. ")
        except ValueError:
            typing_print(f"Please enter a number as a digit, e.g. 1, Commander {name}. ")  
 
def game_start(name):
    """
    Explains rules of the game
    Player selects level of difficulty
    
    """
    print(constants.instructions)
    
    while True:
        answer = typing_input(f"Do you accept the terms of this mission, Commander {name}? ").lower()

        if answer == 'yes':
            typing_print("Great, let's get you spacesuited up!")
            time.sleep(2)
            clear_screen()
            break
        elif answer == 'no': 
            typing_print("That is a shame. Thanks for your time but this is where we go our separate ways.")
            typing_print(f"Goodbye, Commander {name}. This message will self-destruct in 3...")
            time.sleep(1)
            typing_print("2...")
            time.sleep(1)
            typing_print("1...")
            time.sleep(1)
            clear_screen()  
            break
        else:
            typing_print(f"We need a yes or no answer, Commander {name}. ")

def choose_difficulty(name):
    """
    The user chooses level of difficulty.
    Easy, medium or hard.
    The word register will change in difficulty e.g. easy = moon, hard = constellation

    """
    typing_print(f"OK, Commander {name}. We need you to choose your astronaut level. ")

    while True:
        level = typing_input("Are you a Junior, Senior, or Chief? ").capitalize()

        if level == 'Junior' or level == 'Senior' or level == 'Chief':
            typing_print(f"Great, we'll start the mission as a {level} astronaut!")
            time.sleep(2)
            clear_screen()
            return level
        else:
            typing_print(f"We need your answer, Commander {name}. ")

def get_word():
    """
    Randomly selects word from wordlist
    
    """
    word = random.choice(constants.word_list)
    return word.upper()

def play_game(word):
    """
    Word is selected from wordlist.

    """   

    word_completion = "＿" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6

    # print(level)
    print("Introduce game")
    print(word)
    print(constants.display_rocket(tries))
    print(word_completion)
    print("\n")

    while not guessed and tries > 0:
        guess = input("Please guess a letter or word ").upper()
        clear_screen() 
        
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(f"You already tried this letter! {guess}")
            elif guess not in word:
                print(f"{guess} is not in the word") 
                tries -= 1
                guessed_letters.append(guess)
            else:
                print(f"Good job {guess} is in the word!")
                guessed_letters.append(guess)  
                # Update word_completion with the guessed letter
                word_completion = ''.join([guess if letter == guess else word_completion[i] for i, letter in enumerate(word)])
            
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print(f"You already guessed the word {guess}")
            elif guess != word:
                print(f"{guess} is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("Not a valid guess.")
        
        print(constants.display_rocket(tries))
        print(word_completion)
        print("\n")

    if guessed:
        print("Congrats, you guessed the word! You win!")
    else:
        print(f"Sorry, you ran out of tries. The word was {word}. Maybe next time!")






    
# initiate_game()
# name = validate_name()
# validate_plants(name)
# game_start(name)
# level = choose_difficulty(name)

word = get_word()
play_game(word)

