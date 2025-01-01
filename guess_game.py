import random

import score
import utils


def generate_number(difficulty):
    secret_number = random.randint(0, difficulty)
    return secret_number
def get_guess_from_user(difficulty):
    global user_value
    is_valid_input = False
    while not is_valid_input:
        try:
            user_input = input(f"Please choose a number between 0 and {difficulty} : ")
            user_value = int(user_input)
            if 0 <= user_value <= difficulty:
                is_valid_input = True
            else:
                print(f"Invalid input. Please enter a number in range of 0 and {difficulty}")
        except ValueError:
            print(f"Invalid input. Please enter a number in range of 0 and {difficulty}")
    return user_value

def compare_results(secret_number, user_val,difficulty):
    try:
        assert secret_number == user_val
        print(f"You made it, you hit the secret number {secret_number}")
        return True
    except AssertionError:
        return False

def play(difficulty):
    try:
        print (f"User entered difficult level of {difficulty}")
        if difficulty > 0:
            secret_number=generate_number(difficulty)
            user_val= get_guess_from_user(difficulty)
            res= compare_results(secret_number, user_val,difficulty)
            if res == True:
                print("Well done, you guessed well!")
                score.add_score(difficulty)
            else:
                print ("You didn't guess the right number, try again")
                score.add_score(utils.BAD_RETURN_CODE)
        else:
            print (f"Invalid difficulty level entered, please a valid number between 1 and {difficulty}")
    except ValueError:
        print(f"Invalid difficulty level entered, please a valid number between 1 and {difficulty}")
