

def welcome():
    username=input("please state your name: ")
    print(f"Hi {username} and welcome to the World of Games: The Epic Journey")

def start_play():
    print("Please choose a game to play:")
    print("1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back.")
    print("2. Guess Game - guess a number and see if you chose like the computer.")
    print("3. Currency Roulette - try and guess the value of a random amount of USD in ILS")
    game=input("please choose the game (1-3)...")

    if game == '1':
        print ("You selected option 1")
    elif game == '2':
        print ("You selected option 2")
    elif game == '3':
        print ("You selected option 3")
    else:
        print ("Invalid option selected, you must choose option between 1 to 3, exiting...")
        return

    difficulty=input("please choose the game difficulty (1-5)...")
    if (difficulty!=""):
        print (f"Your selected game difficulty level is: {difficulty}")
    else:
        print ("You must specify game difficulty, exiting...")
        return