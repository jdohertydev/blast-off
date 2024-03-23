# Blast Off!

## Overview

‘Blast off!’ is an immersive, educational guessing game for one player with a ‘space and the universe’ theme. Similar to ‘hangman’, the player is presented with a series of underscores that represent a word. They must select letters from the alphabet and guess the word to win. This game is run in a mock terminal deployed by Heroku.

In recent years, the traditional hangman game has fallen out of favour with many educators due to sensitivity to violence and a lack of educational value. As a former teacher, I wanted to recreate something that could be used by any teacher in the classroom or child at home.

Table of Contents
How to Play


Planning Stage
User Story
Site Aims
How Will This Be Achieved
Game Flow Chart

Start
|
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
End

Features
Welcome Screen
How to Play Guide
Game Modes
Game Screen
Playing
Win
Lose
Exit
Future-Enhancements
Testing Phase
Libraries
Python Standard Library
3rd Party Libraries
Deployment to Heroku
Credits