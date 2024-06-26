# Import the random module for random word selction
import random
# Import time, sys and os for typing effect and clear
import time
import sys
import os
# Import constants to get random words and ASCII images
import constants
# Import code to enable press any button to continue
# - https://stackoverflow.com/questions/11876618/python-press-any-key-to-exit
from getch import pause


def typing_print(text):
    """
    https://www.101computing.net/python-typing-text-effect/

    Creates a typing effect to improve user experience.

    """
    for character in text:
        if character == '\n':
            print("\n")
        else:
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


def show_splash_screen():
    """
    Shows logo and rocket graphic and press any button to continue

    """
    print(constants.logo_art)
    print(constants.display_rocket(0))
    pause()
    clear_screen()


def show_welcome_msg():
    """
    Initiates the game.

    """
    typing_print("Welcome to 'Blast Off'!\n")
    typing_print("You have been selected for a very special mission.\n")
    typing_print("Before we tell you more...\n")


def take_name_input():
    """
    Validates that the user enters a name.
    Check if the input is empty or contains only whitespace

    """
    while True:
        name = typing_input("What is your name? ").strip()
        if not name.strip():
            typing_print("We need a valid name, Commander. ")
            continue

        if name.replace(" ", "").isalpha():
            name = name.capitalize()
            typing_print(f"\nThanks, Commander {name}. ")
            typing_print(
                "One more thing. To make sure you are ready for your"
                )
            typing_print("\nmission, we have one more question. ")
            return name
        else:
            typing_print(f"\n{name} isn't a name on our VIP list.\n")
            typing_print("Try again using letters from the alpabet.\n")
            continue


def ask_warmup_question(name):
    """
    Validates that the answer is a digit.

    """
    while True:
        try:
            user_input = int(
                typing_input(constants.WARM_UP_QUESTION_CONFIG["question"])
            )

            if user_input == constants.WARM_UP_QUESTION_CONFIG["answer"]:
                typing_print(
                    f"\nWell done! You know your stuff, Commander {name}. "
                    "Your mission will commence in: \n5...")
                time.sleep(1)
                typing_print("\n4...")
                time.sleep(1)
                typing_print("\n3...")
                time.sleep(1)
                typing_print("\n2...")
                time.sleep(1)
                typing_print("\n1...")
                time.sleep(1)
                clear_screen()
                break
            else:
                typing_print(
                    f"\nHmm, {user_input} isn't quite right, "
                    f"Commander {name}. Try again. ")
        except ValueError:
            typing_print(
                f"\nPlease enter a number as a digit, "
                f"e.g. 1, Commander {name}. ")


def game_start(name):
    """
    Explains rules of the game
    Player selects level of difficulty

    """
    print(constants.instructions)

    while True:
        answer = typing_input(
            f"Do you accept the terms of this mission, "
            f"Commander {name}? ").lower().strip()

        if answer in ['yes', 'y']:
            typing_print("\nGreat, let's get you spacesuited up!")
            time.sleep(2)
            clear_screen()
            break
        elif answer in ['no', 'n']:
            exit_game(name)
        else:
            typing_print(f"\nWe need a yes or no answer, Commander {name}. ")


def choose_difficulty(name):
    """
    The user chooses level of difficulty.
    Easy, medium or hard.
    The word register will change in difficulty:
        e.g. easy = moon, hard = constellation.
    """

    while True:
        level = typing_input(
            f"We need to know what level you are, Commander {name}."
            "\nAre you a Junior, Senior, or Chief? ").capitalize().strip()

        if level in constants.DIFFICULTY_CONFIG.values():
            typing_print(
                f"\nGreat, we'll start the mission as a {level} astronaut!")
            time.sleep(2)
            clear_screen()
            return level
        else:
            typing_print(f"\nWe need your answer, Commander {name}. ")


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


def print_game_status(level, score, tries, word_completion):
    """
    This functions shows game status.

    """
    print(f"Game Mode: {level}")
    print(f"Current Score: {score}")
    print(constants.display_rocket(tries))
    print(word_completion)
    print("\n")


def ask_to_play_again(name, word, level, score):
    """
    Prompts user if they want to play another round or exit.
    """

    while True:
        answer = typing_input("\nDo you want to play again? ").strip().lower()
        if answer in ['yes', 'y']:
            clear_screen()
            return play_game(name, word, level, score)
        elif answer in ['no', 'n']:
            clear_screen()
            exit_game(name)
            return score
        else:
            typing_print("Please enter 'yes' or 'no'.")


def play_game(name, word, level, score=0):
    """
    Adapted from https://www.youtube.com/watch?v=m4nEnsavl6w
    Word is selected randomly from wordlist.
    User has to guess letters or word within 6 turns.

    """
    word = get_word(level)
    word_completion = "＿" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = constants.MAX_TRIES

    print_game_status(level, score, tries, word_completion)

    while not guessed and tries > 0:

        guess = input(
            "Please guess a letter or word or type ABORT "
            "to end the mission.\n ").upper().strip()
        if guess == "ABORT":
            clear_screen()
            return exit_game(name)

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print(f"You already tried this letter! {guess}")
            elif guess not in word:
                print(f"{guess} is not in the word!")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print(f"Good job {guess} is in the word!")
                guessed_letters.append(guess)
                word_completion = ''.join([
                    guess if letter == guess else word_completion[i]
                    for i, letter in enumerate(word)
                ])
                if word_completion == word:
                    guessed = True

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

        time.sleep(1)
        clear_screen()

        print_game_status(level, score, tries, word_completion)

    if guessed:
        typing_print(
            "Congrats, you guessed the word and made the mission! "
            "You get a point! ")
        score += 1
    else:
        print(
            f"Sorry, the rocket left without you. The word was {word}. "
            "Maybe you can crew next time!")

    ask_to_play_again(name, word, level, score)


def exit_game(name):
    """
    Exit game sequence with cool countdown.

    """
    typing_print(
        "That is a shame. Thanks for your time "
        "but this is where we go our separate ways. ")
    typing_print(
        f"Goodbye, Commander {name}. "
        "This message will self-destruct in: \n3...")
    time.sleep(1)
    typing_print("\n2...")
    time.sleep(1)
    typing_print("\n1...")
    time.sleep(1)
    clear_screen()
    typing_print("\nClick 'RUN PROGRAM' to play again.\n")
    return None


def main():
    """
    Excutes all the functions for the game.

    """
    show_splash_screen()
    show_welcome_msg()
    name = take_name_input()
    ask_warmup_question(name)
    game_start(name)
    level = choose_difficulty(name)
    word = get_word(level)
    play_game(name, word, level)


main()
