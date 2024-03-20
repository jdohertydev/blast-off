word_list_easy = [
    "easy", "moon", "planet", "earth", "sun", "meteor", "galaxy", "comet", "star", "rocket"
    ]

word_list_medium = [
    "medium", "astronaut", "orbit", "fuel", "launch", "countdown", "astronomer", "sunlight", "universe"]

word_list_hard = [
    "hard", "cosmology", "extragalactic", "interstellar", "occultation", "spectroscope", "translunar", "giantwormhole", "weightlessness", "totality"
]

instructions ="""
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


    # stages = [
    #     # Stage 6
    #     """
    #     Stage 6 rocket ASCII art
    #     """,
    #     # Stage 5
    #     """
    #     Stage 5 rocket ASCII art
    #     """,
    #     # Stage 4
    #     """
    #     Stage 4 rocket ASCII art
    #     """,
    #     # Stage 3
    #     """
    #     Stage 3 rocket ASCII art
    #     """,
    #     # Stage 2
    #     """
    #     Stage 2 rocket ASCII art
    #     """,
    #     # Stage 1
    #     """
    #     Stage 1 rocket ASCII art
    #     """
    # ]
    return stages[tries]
