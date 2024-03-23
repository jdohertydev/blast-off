# Blast Off!

## Overview

‘Blast off!’ is an immersive, educational guessing game for one player with a ‘space and the universe’ theme. Similar to ‘hangman’, the player is presented with a series of underscores that represent a word. They must select letters from the alphabet and guess the word to win. This game is run in a mock terminal deployed by Heroku.

Screenshot

In recent years, the traditional hangman game has fallen out of favour with many educators due to sensitivity to violence and a lack of educational value. As a former teacher, I wanted to recreate something that could be used by any teacher in the classroom or child at home.

Here is the live version of the game.

## How to Play

The game has been designed to be as simple as possible. The player:

1. Must answer a warm-up question in order to be selected for the mission.
2. Chooses a level of difficulty (junior, senior, chief) – the harder the level, the more abstract the word.
3. Is presented with a series of underscores and must try and guess the word by either selecting individual letters or by 4. writing the word itself.
5. Has 6 turns in order to guess the word. By doing so correctly, the player gets a point. If the player doesn’t, the turn is over, the word is revealed and they can play another round.
6. Has the option to continue playing or exit the game.

## Planning Stage

### User Stories:

As a user, I want to:

* Be fully immersed in a ‘space and the universe’ experience.
* Choose my level of difficulty.
* Receive feedback regarding my progress.
* Easily exit the game.

### Site Aims

The site aims to:

* Never throw an error.
* Create an arcade like feel using basic black and white.
* Use visuals to bring the text to life.

### How Will This Be Achieved:

To achieve the above, the site will:

* Speak directly to the player in the first person after their name has been captured.
* Use a typewriter effect on any dialogues which feels like the message is being written in the moment.
* Clearly show the player’s score, game mode level and used letters.
* Use ASCII art to show the stages of lives lost during game mode.
* Clear the screen on stage changes so not to confuse the player.
* Handle very carefully user input to avoid any errors.
* Be easy for the player to exit the game. There will be ‘getting off’ points during a live game and when the game is over.

## Game Flow Chart

Start

|-----> Show Splash Screen
|         |
|         |-----> Show Logo and Rocket Graphic
|         |
|         |-----> User presses any key to continue
|         |
|         |-----> Clear Screen
|
|-----> Show Welcome Message
|         |
|         |-----> Typing Print: "Welcome to 'Blast Off'!"
|         |
|         |-----> Typing Print: "You have been selected for a very special mission..."
|
|-----> Take Name Input
|         |
|         |-----> Validate Name Input
|                   |
|                   |-----> Typing Input: "What is your name?"
|                   |
|                   |-----> If Name is Valid, Proceed
|                   |
|                   |-----> If Name is Invalid, Retry
|
|-----> Ask Warmup Question
|         |
|         |-----> Typing Input: Display Warmup Question
|         |
|         |-----> Validate User Input
|                   |
|                   |-----> If Correct Answer, Proceed
|                   |
|                   |-----> If Incorrect Answer, Retry
|
|-----> Game Start
|         |
|         |-----> Display Instructions
|         |
|         |-----> User Accepts Mission?
|                   |
|                   |-----> If Yes, Proceed
|                   |
|                   |-----> If No, Exit Game
|
|-----> Choose Difficulty
|         |
|         |-----> User Chooses Difficulty
|                   |
|                   |-----> If Valid Difficulty, Proceed
|                   |
|                   |-----> If Invalid Difficulty, Retry
|
|-----> Get Word (Not visible to the  user)
|         |
|         |-----> Randomly Select Word Based on Difficulty
|
|-----> Play Game
|         |
|         |-----> Loop Until Game Over or User Quits
|                   |
|                   |-----> Display Game Status
|                   |
|                   |-----> Take User Guess
|                   |
|                   |-----> If Guess is Correct, Update Game Status
|                   |
|                   |-----> If Guess is Incorrect, Update Game Status
|                   |
|                   |-----> Check Game Over Conditions
|                             |
|                             |-----> If Game Over, Ask to Play Again
|                             |
|                             |-----> If Continue, Repeat Loop
|
|-----> Exit Game
|         |
|         |-----> Display Farewell Message
|         |
|         |-----> Clear Screen
| 
End\

## Features

### Logo and graphics

* The logo and graphic featured in the splash screen are made in ASCII characters as graphics are not supported in Heroku. This gives the game a classic arcade feeling.

IMAGE

### Press any button to continue

Again, in the spirit of the arcade feeling, the classic “press any button to continue” text is achieved importing a library called ‘getch’ and calling ‘pause’.

IMAGE

### Typewriter effect

A current feature of Chat GPT and numerous classic arcade games, the typewriter effect is used to simulate that mission control is directly talking to the player. This is one of the many ways the game immerses the player within it.

IMAGE

### Clear screen

A simple but key feature is the ‘clear screen’ function. This acts as a signpost for each stage of the game, like a new chapter in a book, and without it, the user will be left with a large amount of text in the terminal. Visually, this is not pretty but it could also confuse the user and take away from the immersive experience.

### Colour
### Capture name variable

When keeping someone’s attention, it is often said that using the person’s name is the most effective way. The ‘take_name_input’ function does this early on in the program and uses it in the script throughout the game using f-strings and `{name}`. 

### Warm-up question

To generate more player engagement, a warm-up question is asked before the player starts the game. Hopefully, the player already knows the answer and will feel even more immersed in the experience.

### Level of user difficulty

All good games normally have a level of mastery as this is what keeps players returning. This game has 3 basic levels (easy, medium and hard) but uses different nomenclature connected to space travel (Junior, Senior and Chief). This feeds back into the primary objective of making this an immersive game. 

### Stages of rocket construction

As the user progresses through a turn, it’s inevitable that they will guess a letter that doesn’t appear in the word. In this case, part of the rocket is constructed using ASCII text. There are 6 stages of construction which represent the number of tries the user has. Without this ASCII imagery, the game would be quite static, and the user could get bored more quickly.

### Game logic

* Random Word Selection: The game selects a word randomly from a wordlist depending on level chosen.
* Limited Guesses: The user has a limited number of tries (6 turns) to guess the word.
* Interactive Guessing: Users can guess individual letters or the entire word.
* Feedback Mechanism: Provides immediate feedback on guesses, informing users whether their guess is correct or incorrect.
* Dynamic Progress Display: Displays the progress of the game through ASCII art, representing the stages of rocket construction.
* Game Over Handling: Handles game over conditions, such as running out of guesses or successfully guessing the word.
* Scoring System: Provides a scoring system where users earn points for successfully guessing the word.
* User Interaction: Utilises user input functions (typing_input) to interact with the user during the game.
* Game Status Display: Continuously displays the game status, including the current score, remaining tries, and the word completion status.
* Game Outcome Notification: Notifies the user of the game outcome, congratulating them for successful guesses or informing them of failure.

### Exit junctions

A good game should have exit junctions built into it. Within this game, the player can exit in multiple scenarios such as during a turn by typing ‘ABORT’ or when a turn is complete. Also, the text used in the exit game function uses a countdown script from 3 to 1, again keeping in the theme of lexis used in space travel.

## Future-Enhancements

In the future, a leader board could be added to show highest scores. As well as this, a 2-player mode could be created so that friends could choose their own words. Finally, having basic audio play per keyboard stroke would add to the immersive experience.

Testing Phase

## Libraries

For this project, these standard libraries were used:

* random: This module is used for random word selection. It allows the program to choose a word randomly from a predefined wordlist.
* time, sys, os: These modules are used for creating typing effects and clearing the screen to enhance the user experience.
    *time: It is used for introducing delays between printing characters to create a typing effect.
    * sys: It provides access to functions that interact with the Python interpreter. In this code, it's used for writing characters to the standard output (sys.stdout) to create the typing effect.
    * os: It provides functions for interacting with the operating system. Here, it's used to clear the screen to improve the visual presentation of the game.

3rd party libraries used are:

* constants: This is a custom module imported from constants.py. It likely contains predefined constants such as word lists, ASCII art, and configuration settings used throughout the game.
* getch: This module contains fthe unctionality for pausing the program until the user presses any key to continue.

## Data model

Overall, the game utilises 4 data models to manage the game's logic, user interaction, and state throughout the gameplay experience.

## Blast Off Game Data Models

### 1. Word List Model

The game randomly selects words from predefined word lists based on the chosen difficulty level. These lists, categorised as `constants.word_list_easy`, `constants.word_list_medium`, and `constants.word_list_hard`, organise words according to their difficulty. Players encounter varying levels of challenge based on their chosen difficulty level.

### 2. User Model

While not explicitly defined in the code, the game interacts with users by collecting their input for their name and responses to questions. This model encompasses user interaction and input validation mechanisms. It ensures that user inputs are processed correctly and meet specific criteria, such as providing a valid name or responding appropriately to in-game prompts.

### 3. Game State Model

Throughout gameplay, the game maintains and updates various states to manage its progression. Key components of this model include:

- **Current Word Being Guessed (`word_completion`)**: Represents the ongoing process of guessing the word, with placeholders for unrevealed letters.
- **Guessed Letters (`guessed_letters`)**: Tracks letters that the player has guessed during the game.
- **Guessed Words (`guessed_words`)**: Stores words that the player has guessed.
- **Remaining Attempts (`tries`)**: Monitors the number of remaining attempts or guesses available to the player. 

These components collectively define the game's state at any given moment, reflecting the progress and status of the ongoing gameplay session.

### 4. Score Model

The game features a scoring system that rewards players for correctly guessing words. As players make correct guesses, their score increases, reflecting their progress and success within the game. This model serves to incentivise players and provides a metric for tracking their performance and achievements.

## Testing

## Deployment to Heroku (working 23 March 2024)

The project was deployed to Heroku using the following steps adapted from taken from [ilyasolgun11](https://github.com/ilyasolgun11/hangman/tree/main?tab=readme-ov-file#deployment-to-heroku):

1. **Log in to Heroku** or create an account if required.
2. Click on the **dashboard** from the hamburger menu on the top right to navigate to the apps page.
3. Click the **new button** on the top right of the page.
4. Select the "**create new app**" option.
5. Enter the **app name**. I named mine 'Blast Off!' (this has to be unique).
6. Once Heroku accepts the app name, **select your region**.
7. Click the **purple Create app button** when you are ready to proceed.
8. This will bring you to the **project Deploy tab**. From here, navigate to the **settings tab** and scroll down to the **Config Vars section**.
9. Click the button labeled **Reveal Config Vars**, Enter the key as **Port**, the Value as **8000**, and Click the **add button**.
10. Scroll down to the **buildpacks section** of the settings page, click the button labeled **Add buildpack**, select **Python**, and click **Save Changes**.
11. Repeat **step 10** but this time add **Node.js** instead of Python.
12. Remember to keep the buildpacks in the correct order, **Python first** and **Node second**.
13. Scroll back to the top of the settings page and navigate to the **Deploy tab**.
14. From the deploy tab, select **GitHub** as the deployment method.
15. Confirm you want to connect to GitHub.
16. Search for the **repository name** and click the **connect button** next to the intended repository.
17. From the bottom of the deploy page, select your preferred deployment type by following one of the steps below:
    - Clicking either "**Enable Automatic Deploys**" for automatic deployment when you push updates to GitHub.
    - Select the correct branch for deployment from the drop-down menu and click the "**Deploy Branch**" button for manual deployment.

## Credits


    ilyasolgun11  https://github.com/ilyasolgun11/hangman/tree/main?tab=readme-ov-file#deployment-to-heroku