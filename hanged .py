import sys

def hangman():
    print(""" _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                        _                                             

""") 

    print("")
    character_list = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," "]
     
    phrase = input("Player 1, please enter a word or a short phrase: ")

    while True:  
        for char in phrase.lower():
            if char not in character_list:
                print("Your phrase contains invalid characters. Please don't use any punctuation or numbers and try again.")
                phrase = input("Player 1, please enter a word or a short phrase: ")  
        break
    print("")
            
    start(phrase) #start guessing game


def start(phrase):
    guesses = ''
    spaces = 0

    for char in phrase:
        if char == " ":
            spaces = spaces + 1

    character_list = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," "]

    lives = int(input("Player 1, how many lives does Player 2 have? (1-9): "))
    
    while True: 
        if lives not in range(1,10):
            print("You have entered an invalid number of lives, try again. Only 1 - 9 allowed")
            lives = int(input("Player 1, how many lives does Player 1 have? (1-9): "))
        else:
            break
        
    #print 40 lines so the input from player 1 is moved up and becomes invisible to player 2
    print(40* "\n")
  

    while True: #repeat forever
        count = 0 
        print("")
        character = input("Player 2, guess a character: " )
        print("")

        while True:
            if character.lower() not in character_list:
                print("The character you have guessed is not valid. Please don't use any punctuation or numbers.")
                print("")
                character = input("Player 2, guess a character: " )
            else:
                break
            
        for char in phrase:
            if character in char:
                count = count + 1
                guesses = guesses + character
            elif character not in char:
                count == 0

        for char in phrase:
            if char in guesses:
                print(char + " " , end='')
            elif char not in guesses:
                if char == " ": 
                    print(" ", end='')
                else:
                    print("_ ", end='' )
                
        if count == 0:
            print("")
            print("The character doesn't exist in the phrase")
            lives = lives - 1
            print("You have lost a life. You have", lives, " lives left") 
            print("")

        elif count > 0:
            print("")
            print("The character exists in the phrase", count, "time(s)") 

        if len(guesses) + spaces == len(phrase):
            win(phrase)

        if lives == 0: 
            lose(phrase)

        art(lives)
            

    
        print("")            
def art(lives):
    if lives == 9:
        print(
    """
 ------
|     |
|
|
|
|
|
|
----------
""")
    elif lives == 8:
        print(
"""
 ------
|     |
|     0
|
|
|
|
|
----------
""")
    elif lives == 7:
        print(
"""
 ------
|     |
|     0
|     +
|
|
|
|
----------
""")
    elif lives == 6:
        print(
"""
 ------
|     |
|     0
|    /+
|
|
|
|
----------
""")
    elif lives == 5:
        print("""
 ------
|     |
|     0
|    /+\ 
|
|
|
|
----------
""")
    elif lives == 4:
        print(
"""
 ------
|     |
|     0
|    /+\  
|     |  
|
|
|
----------
""")
    elif lives == 3:
        print(
"""
 ------
|     |
|     0
|    /+\  
|     |  
|     |   
|
|
----------
""")
        
    elif lives == 2:
        print(
"""
 ------
|     |
|     0
|    /+\
|     |
|     |
|    /
|
----------
""")
    elif lives == 1:
        print(
"""
  ------
|     |
|     |
|     0
|    /+\  
|     |   
|     |  
|    / \   
|
----------
""")
    elif lives == 0:
        print(
"""
  ------
|     |
|     |
|     0
|    /+\
|     |
|    / \
|
 HANGED MAN
----------
""")
        

def win(phrase):
    print("")
    print("Player 2 wins!!! The phrase was: ",phrase)
    print("")
    choice = int(input("Would you like to play again? 1 = YES, 0 = NO :"))

    while True: 
        if choice == 1:
            hangman()
        elif choice == 0:
            print("Goodbye!") 
            sys.exit()
        else:
            print("You have entered an invalid choice. Please try again.")
            choice = int(input("Would you like to play again? 1 = YES, 0 = NO :"))

def lose(phrase):
    print("")
    print(""" 	
                 uuuuuuu
             uu$$$$$$$$$$$uu
          uu$$$$$$$$$$$$$$$$$uu
         u$$$$$$$$$$$$$$$$$$$$$u
        u$$$$$$$$$$$$$$$$$$$$$$$u
       u$$$$$$$$$$$$$$$$$$$$$$$$$u
       u$$$$$$$$$$$$$$$$$$$$$$$$$u
       u$$$$$$"   "$$$"   "$$$$$$u
       "$$$$"      u$u       $$$$"
        $$$u       u$u       u$$$
        $$$u      u$$$u      u$$$
         "$$$$uu$$$   $$$uu$$$$"
          "$$$$$$$"   "$$$$$$$"
            u$$$$$$$u$$$$$$$u
             u$"$"$"$"$"$"$u
  uuu        $$u$ $ $ $ $u$$       uuu
 u$$$$        $$$$$u$u$u$$$       u$$$$
  $$$$$uu      "$$$$$$$$$"     uu$$$$$$
u$$$$$$$$$$$uu    '''''    'uuu$$$$$$$$$'
'$$$"$$$$$$$$$$u'   'u$$$$$$$$$"$$$'
 ""      "$$$$$$$$$$$uuuuu""
           'uuuu"$$$$$$$$uuu
  "u$$$uuu$$$$$$$$$uu $$$$$$$$$$$uuu$$$'
  "$$$$$$$$$$           ""$$$$$$$$$$$'
   "$$$$$"                      "$$$$'
     '$$$"                         $$$ """)  
    print("You lost! Player 1 wins!!! The phrase was:", phrase)
    print("")
    choice = int(input("Would you like to play again? 1 = YES, 0 = NO :"))

    while True: 
        if choice == 1:
            hangman()
        elif choice == 0:
            print("Goodbye!") 
            sys.exit()
        else:
            print("You have entered an invalid choice. Please try again.")
            choice = int(input("Would you like to play again? 1 = YES, 0 = NO :"))    

    
    
hangman() 

