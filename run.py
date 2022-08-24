import os
import random
from words import WORDS
from hangman import hangman

RED_COLOR = '\033[0;31m'
YELLOW_COLOR = '\033[0;33m'


def start_screen():
    """
    Sets a function for when a user arrives on the start screen,
    asks the user for there name and welcomes user.
     - name input feild only accepts letters
    """
    print(RED_COLOR +
        """
           ___ _          _     _                      
          / __\ |__  _ __(_)___( )__                   
         / /  | '_ \| '__| / __|/ __|                  
        / /___| | | | |  | \__ \\__ \                  
        \____/|_| |_|_|  |_|___/|___/                  
                                                   
          /\  /\__ _ _ __   __ _ _ __ ___   __ _ _ __  
         / /_/ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
        / __  / (_| | | | | (_| | | | | | | (_| | | | |
        \/ /_/ \__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                           |___/                     
        """                                           
        )

    while True:
        name = input(YELLOW_COLOR + "Please Enter Your Name:\n")
        
        if not name.isalpha():
            print("Name must be letters only\n")
        else:
            print(f"Hello {name}, Welcome to Chris's Hangman and Good Luck!\n")
            menu()


def menu():
    """
    menu function which gives the user two options
    - Press 1 to play or 2 for instructions
    - only accepts valid keys or error message comes up
    """
    while True:
        user_input = input("Press P to Play game\nPress I for Instructions\n").upper()
        if user_input == "P":
            play_game #undefined variable to add later on
        elif user_input == "I":
            print(
                "1.The computer will generate a random word and it's\n"
                "your task to guess the letters from the word.\n"
                "2.To guess, type a letter of your choice and hit enter.\n"
                "3.If you guess correctly, the letter will be revealed.\n"
                "4.If you guess incorrectly, you will lose a life and \n"
                " the Hangman will start to appear.\n"
                "5.You have 8 lives to guess the correct word.\n"
    
                "Good Luck!\n")
            enter_input = input("Press Enter to go back to the menu\n").upper()
            if enter_input == "":
                menu()
            else:
                print(RED_COLOR + "Oops look's like you pressed the wrong key!\n")
                
        else:
            print("Invalid Character, please try again!\n")
            
def randomword():
    """
    A function that chooses a random word from words.py
    """
    word = random.choice(WORDS).upper()



