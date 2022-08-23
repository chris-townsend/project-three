def start_game():
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
            print(f"Hello {name}, Welcome to Hangman and Good Luck!")
            break
            


    


print(start_game())