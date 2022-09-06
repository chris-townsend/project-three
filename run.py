"""
random module used to generate a random word from words.py
os module used to generate colours and clear the console
"""
import random
import os
from words import WORDS
from diagrams import player_lost, player_won, header
from hangman import hangman

YELLOW = '\033[33m'
RED = '\033[0;31m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
CBLINK = '\33[5m'

LIVES = 8
GAME_WON = False
word = random.choice(WORDS)
word = word.upper()
REVEAL = list(len(word)*'_')


def ask_for_name():
    """
    Ask a user for there name on game start up,
    - isalpha() used to only accept letters.
    When user enters name correctly, clear console and
    welcome user with welcome message, hangman diagram and menu option
    """
    while True:
        name = input(YELLOW + "Please Enter Your Name:\n")
        if not name.isalpha():
            print(RED + "Name must be letters only\n")
            return ask_for_name()
        if name.isalpha():
            os.system("clear")
            header()
            print(hangman[8-LIVES])
            print("\n")
            print(YELLOW + f"Hello {name}, "
                  "Welcome to Chris's Hangman and Good Luck!\n")
            menu()
            break
        return


def menu():
    """
    menu function which gives the user two options
    - Press 1 to play or 2 for instructions
    - only accepts valid keys or error message comes up
    """
    while True:
        user_input = input(YELLOW + "Press P to Play game\n"
                           "Press I for Instructions\n").upper()
        if user_input == "P":
            break

        elif user_input == "I":
            os.system("clear")
            header()
            print(YELLOW +
                  "1.The computer will generate a random word and it's\n"
                  "your task to guess the letters from the word. If your "
                  "feeling confident, guess the whole word!\n"
                  "\n"
                  "2.To guess, type a letter or word of your choice and hit "
                  "enter.\n"
                  "\n"
                  "3.If you guess correctly, the letter or word will be "
                  "revealed.\n"
                  "\n"
                  "4.If you guess incorrectly, you will lose a life and \n"
                  " the Hangman will start to appear.\n"
                  "\n"
                  "5.You have 8 lives to guess the correct word.\n"
                  "Good Luck!\n")
            enter_input = input("Press Enter to go back to the menu\n").upper()
            if enter_input == "":
                os.system("clear")
                header()
                print(hangman[8-LIVES])
                menu()
                break
            else:
                print(RED + "Oops look's like you pressed the wrong key!\n")
        else:
            print(RED + "Invalid Character, please try again!\n")


def restart_game():
    """
    Function to restart game at end of play
    Gives the user two options, Y to play again or
    N to clear the console and return to menu with hangman diagram
    Incorrect letter results in ValueError message
    """
    game_restart = False

    while not game_restart:
        restart = input(YELLOW + "Would you like to play again?"
                        "Y/N").upper()
        try:
            if restart == "Y":
                return True
            elif restart == "N":
                game_restart = True
                os.system("clear")
                header()
                print(hangman[8-LIVES])
                menu()
                return True
            else:
                raise ValueError("You must type in Y or N")

        except ValueError:
            print("\n You must type in Y or N Please try again.\n")


header()
ask_for_name()


def display():
    """
    Clears the console and displays the hangman diagram
    depending on how many lives left and guesses taken
    Reveals a letter if the letters within the correct word
    """
    os.system("clear")
    header()
    print(hangman[8-LIVES])
    print(' '.join([str(e) for e in REVEAL]))
    print(f"You have {LIVES} lives")


def check_letter(letter, key_word):
    """
    A function that checks if the letter is within the key_word
    Function returns True if won
    """
    for i, letter in enumerate(key_word, 0):
        letter = key_word[i]
        if guess == letter:
            REVEAL[i] = guess
    if '_' not in REVEAL:
        return True
    else:
        return False


# Main Game logic which checks if word has been guessed
# within 8 lives
# Prints either player_won or player_lost at end of gameplay,
# with a choice to restart


while GAME_WON is False and LIVES > 0:
    display()
    guess = input(WHITE + 'Guess a letter or an entire word:')
    guess = guess.upper()
    if guess == word:
        GAME_WON = True
        reveal = word
    elif len(guess) == 1 and guess in word:
        GAME_WON = check_letter(guess, word)
    else:
        LIVES -= 1
    if GAME_WON:
        print("\n")
        print(YELLOW + "W E L L  D O N E")
        player_won()
        print(f"you guessed the correct word ~ {word} with {LIVES} lives left")
        print(CYAN + "=============================================\n")
    elif LIVES == 0:
        print("\n")
        print(RED + "Y O U  F A I L E D")
        player_lost()
        print(RED + f"you ran out of lives ~ the word was: {word}")
        print(CYAN + "=============================================\n")
    if GAME_WON is True or LIVES <= 0:        # Conditioned restart
        if restart_game() is True:
            GAME_WON = False
            LIVES = 8
            word = random.choice(WORDS)
            word = word.upper()
            REVEAL = list(len(word)*'_')
