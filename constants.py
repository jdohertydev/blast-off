word_list_easy = [
    "easy"
    ]

word_list_medium = [
    "medium"]

word_list_hard = [
    "hard"
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
Stage 6 rocket ASCII art
                """,
                # Stage 5 rocket ASCII art
                """
Stage 5 rocket ASCII art
                """,
                # Stage 4 rocket ASCII art
                """
Stage 4 rocket ASCII art
                """,
                # Stage 3 rocket ASCII art
                """
Stage 3 rocket ASCII art
                """,
                # Stage 2 rocket ASCII art
                """
Stage 2 rocket ASCII art
                """,
                # Stage 1 rocket ASCII art
                """
Stage 1 rocket ASCII art
                """,
                # Stage 0 rocket ASCII art
                """
Stage 0 rocket ASCII art
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
