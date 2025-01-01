import currency_roulette_game
import guess_game
import memory_game


def welcome():
    username = input("please state your name: ")
    print(f"Hi {username} and welcome to the World of Games: The Epic Journey")


def start_play():
    print("""Please choose a game to play:
    1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back.
    2. Guess Game - guess a number and see if you chose like the computer.)
    3. Currency Roulette - try and guess the value of a random amount of USD in ILS""")

    # Initialize flags for loop control
    is_valid_game = False
    is_valid_difficulty = False

    game_value = None
    difficulty_value = None

    # Validate game type input
    while not is_valid_game:
        try:
            game = input("Please choose the game type you wish to play (1-3)")
            game_value = int(game)
            if 1 <= game_value <= 3:
                is_valid_game = True
            else:
                print("Invalid input. Please enter a number in range of 1-3")
        except ValueError:
            print("Invalid input. Please enter a number in range of 1-3")

    # Validate difficulty number input
    while not is_valid_difficulty:
        try:
            diff = input("please choose the game difficulty (1-5)...")
            difficulty_value = int(diff)
            if 1 <= difficulty_value <= 5:
                is_valid_difficulty = True
            else:
                print("Invalid input. Please enter a valid difficulty in range of 1-5.")
        except ValueError:
            print("Invalid input. Please enter a valid difficulty in range of 1-5.")

    print(f"You entered game type: {game_value} and difficulty level: {difficulty_value}.")
    if game_value == 1:
        memory_game.play(difficulty_value)
    elif game_value == 2:
        guess_game.play(difficulty_value)
    elif game_value == 3:
        currency_roulette_game.play(difficulty_value)
    else:
        return "Invalid option selected"


welcome()
start_play()
exit(0)
