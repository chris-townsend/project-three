"""
Hangman diagrams for incorrect guesses,
Variables WHITE and RED used to add colour
"""
WHITE = '\033[37m'
RED = '\033[0;31m'

hangman = {
           1: WHITE + """
             ________
              |/
              |
              |
              |
              |
              |
              ====== """,

           2: WHITE + """
             ________
              |/    |
              |
              |
              |
              |
              |
              ====== """,

           3: WHITE + """
             ________
              |/    |
              |     O
              |
              |
              |
              |
              ====== """,

           4: WHITE + """
             ________
              |/    |
              |     O
              |
              |
              |
              |
              ====== """,

           5: WHITE + """
             ________
              |/    |
              |     O
              |    /|
              |
              |
              |
              ====== """,

           6: WHITE + """
             ________
              |/    |
              |     O
              |    /|\\
              |
              |
              |
              ====== """,

           7: WHITE + """
             ________
              |/    |
              |     O
              |    /|\\
              |     |
              |
              |
              ====== """,

           8: RED + """
             ________
              |/    |
              |     O
              |    /|\\
              |     |
              |    /
              |
              ====== """,
           9: RED + """
             ________
              |/    |
              |     O
              |    /|\\
              |     |
              |    / \\
              |
              ====== """
          }
