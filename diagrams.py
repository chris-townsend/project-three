RED_COLOR = '\033[0;31m'


def header():
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





def player_lost():
    print (
        """
           ___                                           
          / _ \__ _ _ __ ___   ___    _____   _____ _ __ 
         / /_\/ _` | '_ ` _ \ / _ \  / _ \ \ / / _ \ '__|
         / /_\\ (_| | | | | | |  __/ | (_) \ V /  __/ |   
        \____/\__,_|_| |_| |_|\___|  \___/ \_/ \___|_|   
           """                                    
          )

def player_won():
    print (
        """
        __   __            _    _ _       _ 
        \ \ / /           | |  | (_)     | |
         \ V /___  _   _  | |  | |_ _ __ | |
          \ // _ \| | | | | |/\| | | '_ \| |
          | | (_) | |_| | \  /\  / | | | |_|
          \_/\___/ \__,_|  \/  \/|_|_| |_(_)
          """
          )