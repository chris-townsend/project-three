import os
import random
from words import WORDS
from diagrams import player_lost, player_won, header
from hangman import hangman

YELLOW_COLOR = '\033[0;33m'


def play():
    os.system("clear")
    header()
    print(hangman[8-lives])
    print(' '.join([str(e) for e in reveal]))
    print(f"You have {lives} lives")


def ask_for_name():
    while True:
        name = input(YELLOW_COLOR + "Please Enter Your Name:\n")
        
        if not name.isalpha():
            print("Name must be letters only\n")
        else:
            os.system("clear")
            header()
            print(f"Hello {name}, Welcome to Chris's Hangman and Good Luck!\n")
            menu()
        return


def menu():
    """
    menu function which gives the user two options
    - Press 1 to play or 2 for instructions
    - only accepts valid keys or error message comes up
    """
    while True:
        user_input = input("Press P to Play game\nPress I for Instructions\n").upper()
        if user_input == "P":
            lives = 8
            game_is_won = False
            break

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



word = "dog" #random.choice(WORDS)
word = word.upper()
reveal = list(len(word)*'_')
lives = 8
game_is_won = False

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
        restart = input("Would you like to play again?"
                        "Y/N").upper()
        try:
            if restart == "Y":
                game_restart = True

                play()

            elif restart == "N":
                game_restart = True
                print("\n")
                header()
                ask_for_name()
                menu()

            else:
                raise ValueError(
                "You must type in Y or N"
                )

        except ValueError as e:
            print("\n You must type in Y or N Please try again.\n")


header()
ask_for_name()




while game_is_won == False and lives > 0:
    play()
    guess = input('Guess a letter or an entire word:')
    guess = guess.upper()

    if guess == word:
        game_is_won = True
        reveal = word
    elif len(guess) == 1 and guess in word:
        game_is_won = check_letter(guess, word)
    else:
        lives -= 1

    if game_is_won:
        player_won()
        print("WELL DONE")
        
    else:
        player_lost()
        print(f"YOU FAILED the word was: {word}")
        

restart_game()













