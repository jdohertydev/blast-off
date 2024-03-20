# Import the random module for random word selction
# Import time, sys and os for typing effect and clear
# Import constants to get random words and ASCII images

import random
import time,sys
import os
import constants

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
            exit_game(name)
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

def get_word(level):
    """
    Randomly selects word from wordlist.
    The word selected depends on level choosen.
    
    """
    if level == "Junior":
        word_list = constants.word_list_easy
    elif level == "Senior":
        word_list = constants.word_list_medium
    elif level == "Chief":
        word_list = constants.word_list_hard
    else:
        print("Invalid difficulty level provided.")
        return None

    word = random.choice(word_list) 
    return word.upper()

def play_game(word, level, score=0):
    """
    Adapted from https://www.youtube.com/watch?v=m4nEnsavl6w
    Word is selected randomly from wordlist.
    User has to guess letters or word within 6 turns.
    """   

    word_completion = "＿" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6

    
    print(f"Game Mode: {level}")
    print(f"Current Score: {score}")
    print(constants.display_rocket(tries))
    print(word_completion)
    print("\n")

    while not guessed and tries > 0:
        
        guess = input("Please guess a letter or word or type ABORT to end the mission. ").upper()

        if guess == "ABORT":
            clear_screen()
            return exit_game(name)            
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
        
        
        
        print(f"Game Mode: {level}")
        print(f"Current Score: {score}")
        print(constants.display_rocket(tries))
        print(word_completion)
        print("\n")

    if guessed:
        print("Congrats, you guessed the word and made the mission! You get a point!")
        score +=1
    else:
        print(f"Sorry, the rocket left without you. The word was {word}. Maybe you can crew next time!")

    while True:
        answer = input("Do you want to play again? (yes/no): ").strip().lower()
        if answer == 'yes':
            clear_screen() 
            return play_game(word, level, score) 
        elif answer == 'no':
            clear_screen()
            exit_game(name)  
            return score  
        else:
            print("Please enter 'yes' or 'no'.")
    



def exit_game(name):
    typing_print("That is a shame. Thanks for your time but this is where we go our separate ways. ")
    typing_print(f"Goodbye, Commander {name}. This message will self-destruct in 3...")
    time.sleep(1)
    typing_print("2...")
    time.sleep(1)
    typing_print("1...")
    time.sleep(1)
    clear_screen()  
    return None

initiate_game()
name = validate_name()
validate_plants(name)
game_start(name)
level = choose_difficulty(name)
word = get_word(level)
play_game(word, level)