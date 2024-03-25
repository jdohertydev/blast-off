word_list_easy = [
    "fuel", "moon", "planet", "earth", "sun",
    "meteor", "galaxy", "comet", "star", "rocket"
]

word_list_medium = [
    "spaceship", "astronaut", "orbit", "fuel", "launch",
    "countdown", "astronomer", "sunlight", "universe"
]

word_list_hard = [
    "intergalactic", "cosmology", "extragalactic", "interstellar",
    "occultation", "spectroscope", "translunar",
    "giantwormhole", "weightlessness", "totality"
]

logo_art = """
__________.__                  __    ________   _____  _____
\______   \  | _____    _______/  |_  \_____  \_/ ____\/ ____\\
 |    |  _/  | \__  \  /  ___/\   __\  /   |   \   __\\   __\ 
 |    |   \  |__/ __ \_\___ \  |  |   /    |    \  |   |  |   
 |______  /____(____  /____  > |__|   \_______  /__|   |__|   
        \/          \/     \/                 \/              
"""

instructions = """
+------------------------------------------------------------+
|              CLASSIFIED - MISSION OBJECTIVE                |
+------------------------------------------------------------+
| Guess the space-related word before the spaceship          |
| blasts off into orbit.                                     |
|                                                            |
| * Choose your level of difficulty (easy, medium, or hard). |
| * You have 6 opportunities to guess.                       |
| * You get one point if you guess the word correctly        |
| * The number of spaces represents the word length.         |
| * You can either select letters or guess the word outright.|
| * If after 6 turns you don't guess correctly, the mission  |
| starts without you.                                        |
+------------------------------------------------------------+
"""

WARM_UP_QUESTION_CONFIG = {
     "question": "\nHow many planets are there in our Solar System? ",
     "answer": 9,
}

DIFFICULTY_CONFIG = {
     "easy": 'Junior',
     "medium": 'Senior',
     "hard": 'Chief'
}

MAX_TRIES = 6

def display_rocket(tries):

    stages = [  # Stage 6 rocket ASCII art
                """
                                //\\
                               //  \\
                          ||  //    \\
                          || //______\\
                          |||         |
                         |  |         |
                         |  |         |
                         |__|________ |
                         |___________ |
                         |  |         |
                         |__|   ||   | \\
                          |||   ||   |  \\
                         //|||   ||   |  \\
                        //_|||...||...|___\\
                          |||::::::::|
                          || \\:::::://
                          ||  ||__||
                          ||    ||
                          ||     \\\\_______________
           _______________||______`---------------

                """,
                # Stage 5 rocket ASCII art
                """
                          ||
                          || 
                          ||         
                         |  |        |
                         |  |        |
                         |__|________|
                         |___________|
                         |  |        |
                         |__|   ||   |\\
                          |||   ||   | \\
                         //|||   ||   |  \\
                        //_|||...||...|___\\
                          |||::::::::|
                          || \\:::::://
                          ||  ||__||
                          ||    ||
                          ||     \\\\_______________
           _______________||______`---------------

                """,
                # Stage 4 rocket ASCII art
                """
                          ||  
                          || 
                          |||        
                         |  |
                         |  |
                         |  |________
                         |__|________|
                         |  |        |
                         |__|   ||   |\\
                          |||   ||   | \\
                          |||   ||   |  \\
                          |||...||...|___\\
                          |||::::::::|
                          || \\:::::://
                          ||  ||__||
                          ||    ||
                          ||     \\\\_______________
           _______________||______`---------------

                """,
                # Stage 3 rocket ASCII art
                """
                          ||  
                          || 
                          ||
                         |  |
                         |  |
                         |  |
                         |  |
                         |  |        
                         |__|   ||   |
                          |||   ||   |
                          |||   ||   |
                          |||...||...|
                          |||::::::::|
                          || \\:::::://
                          ||  ||__||
                          ||    ||
                          ||     \\\\_______________
           _______________||______`---------------

                """,
                # Stage 2 rocket ASCII art
                """
                          ||  
                          || 
                          ||
                         |  |
                         |  |
                         |  |
                         |  |
                         |  |
                         |__|
                          ||
                          ||
                          ||
                          ||
                          || 
                          ||  ||__||
                          ||    ||
                          ||     \\_______________
           _______________||______`---------------

                """,
                # Stage 1 rocket ASCII art
                """
                          ||
                          || 
                          ||
                         |  |
                         |  |
                         |  |
                         |  |
                         |  |
                         |__|
                          ||
                          ||
                          ||
                          ||
                          ||
                          ||
                          ||
                          ||     
           _______________||______

                """,
                # Stage 0 rocket ASCII art
                """
                          ||
                          ||
                          ||
                          ||
                          ||
                          ||
                          ||
                          ||     
           _______________||______

                """
    ]
    return stages[tries]
