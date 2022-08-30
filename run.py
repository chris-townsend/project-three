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

word = random.choice(WORDS)
word = word.upper()
reveal = list(len(word)*'_')
lives = 8
game_is_won = False


def ask_for_name():
    while True:
        name = input(YELLOW + "Please Enter Your Name:\n")
        
        if not name.isalpha():
            print("Name must be letters only\n")
        else:
            os.system("clear")
            header()
            print(hangman[9-lives])
            print(YELLOW + f"Hello {name}, Welcome to Chris's Hangman and Good Luck!\n")
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
        user_input = input(YELLOW + "Press P to Play game\nPress I for Instructions\n").upper()
        if user_input == "P":
            lives = 8
            game_is_won = False
            break

        elif user_input == "I":
            os.system("clear")
            header()
            print( YELLOW +
                "1.The computer will generate a random word and it's\n"
                "your task to guess the letters from the word.\n"
                "\n"
                "2.To guess, type a letter of your choice and hit enter.\n"
                "\n"
                "3.If you guess correctly, the letter will be revealed.\n"
                "\n"
                "4.If you guess incorrectly, you will lose a life and \n"
                " the Hangman will start to appear.\n"
                "\n"
                "5.You have 8 lives to guess the correct word.\n"
    
                "Good Luck!\n")
            enter_input = input("Press Enter to go back to the menu\n").upper()
            if enter_input == "":
                menu()
                break
            else:
                print(RED + "Oops look's like you pressed the wrong key!\n")
                
        else:
            print("Invalid Character, please try again!\n")


def check_letter(letter, word):
    global reveal
    for i in range(0,len(word)):
        letter = word[i]
        if guess == letter:
            reveal[i] = guess
    if '_' not in reveal:
        return True
    else:
        return False


def restart_game():
    """
    Gives player option to restart, otherwise returns to menu
    """
    game_restart = False

    while not game_restart:
        restart = input(YELLOW +"Would you like to play again?"
                        "Y/N").upper()
        try:
            if restart == "Y":
                return True
                play()
            elif restart == "N":
                game_restart = True
                print("\n")
                header()
                menu()
                return True
            else:
                raise ValueError(
                "You must type in Y or N"
                )

        except ValueError as e:
            print("\n You must type in Y or N Please try again.\n")


header()
ask_for_name()

def play():
    os.system("clear")
    header()
    print(hangman[9-lives])
    print(' '.join([str(e) for e in reveal]))
    print(f"You have {lives} lives")


while game_is_won == False and lives > 0:
    play()
    guess = input(WHITE +'Guess a letter or an entire word:')
    guess = guess.upper()

    if guess == word:
        game_is_won = True
        reveal = word
    elif len(guess) == 1 and guess in word:
        game_is_won = check_letter(guess, word)
    else:
        lives -= 1

    if game_is_won:
        print("\n")
        print(YELLOW + "W E L L  D O N E")
        player_won()
        print(f"you guessed the correct word ~ {word} with {lives} lives left")
        print(CYAN + "=============================================\n")
        
    else:
        print("\n")
        print(RED + "Y O U  F A I L E D")
        player_lost()
        print(RED + f"you ran out of lives ~ the word was: {word}")
        print(CYAN + "=============================================\n")
        
    if game_is_won == True or lives <=0:        # Conditioned restart
        if restart_game() == True:
            game_is_won = False
            lives = 8
            reveal = list(len(word)*'_')
















