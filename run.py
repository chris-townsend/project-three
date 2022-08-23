def start_screen():
    """
    Sets a function for when a user arrives on the start page,
    asks the user for there name and welcomes user.
     - name input feild only accepts letters
    gives two options, 1 to play or 2 for instructions
    """
    print(
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
        name = input("Please Enter Your Name:\n")
        
        if not name.isalpha():
            print("Name must be letters only\n")
        else:
            print(f"Hello {name}, Welcome to Chris's Hangman and Good Luck!\n")
            break

    while True:
        user_input = input("Press P to Play game\nPress I for Instructions\n").upper()
        if user_input == "P":
            play_game #undefined variable to add later on
        elif user_input == "I":
            print("Instruction List............")
            break
        else:
            print("Invalid Character, please try again!\n")

            


    


print(start_screen())