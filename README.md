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
### Press any button to continue
### Typewriter effect
### Clear screen
### Colour
### Capture name variable
### Warm-up question
### Level of user difficulty
### Stages of rocket construction
### Game logic
* Point
* Validation
### Exit junctions



Future-Enhancements
Testing Phase
Libraries
Python Standard Library
3rd Party Libraries
Deployment to Heroku
Credits


    ilyasolgun11  https://github.com/ilyasolgun11/hangman/tree/main?tab=readme-ov-file#deployment-to-heroku