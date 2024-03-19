word_list = [
    "test",
    "hello",
    "goodbye"
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
| * The number of spaces represents the word length.         |
| * You can either select letters or guess the word outright.|
| * If after 6 turns you don't guess correctly, the mission  |
| starts without you.                                        |
+------------------------------------------------------------+
"""

def display_rocket(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                    """
                    --------
                    |      |
                    |      O
                    |     \\|/
                    |      |
                    |     / \\
                    -
                    """,
                    # head, torso, both arms, and one leg
                    """
                    --------
                    |      |
                    |      O
                    |     \\|/
                    |      |
                    |     / 
                    -
                    """,
                    # head, torso, and both arms
                    """
                    --------
                    |      |
                    |      O
                    |     \\|/
                    |      |
                    |      
                    -
                    """,
                    # head, torso, and one arm
                    """
                    --------
                    |      |
                    |      O
                    |     \\|
                    |      |
                    |     
                    -
                    """,
                    # head and torso
                    """
                    --------
                    |      |
                    |      O
                    |      |
                    |      |
                    |     
                    -
                    """,
                    # head
                    """
                    --------
                    |      |
                    |      O
                    |    
                    |      
                    |     
                    -
                    """,
                    # initial empty state
                    """
                    --------
                    |      |
                    |      
                    |    
                    |      
                    |     
                    -
                    """
        ]
    return stages[tries]
