from random import randint
from currency_converter import CurrencyConverter

from Flask_Web import score
import utils


def compare_results(user_guess, valid_answers,difficulty):
    try:
        if valid_answers[0] <= user_guess <= valid_answers[1]:
            print("Your guess is in the allowed interval!")
            score.add_score(difficulty)
            return True
        else:
            print("Your guess is NOT IN the allowed interval!")
            score.add_score(utils.BAD_RETURN_CODE)
            return False
    except AssertionError:
        print(f"Your guess exceeds the allowed interval! {valid_answers}")
        return False


def get_money_interval(difficulty):
    rand_dollars = randint(1, 100)
    #initialization
    converter = CurrencyConverter()
    from_cur = "USD"
    to_cur = "ILS"
    print(f"Converting {rand_dollars} to ILS")
    converted_amount = int(converter.convert(rand_dollars, from_cur, to_cur))
    print(f"{rand_dollars} {from_cur} is equal to {converted_amount} {to_cur}")

    #calculate allowed answer (interval) based on difficulty - (10-difficulty)
    interval = int(10 - difficulty)
    min = converted_amount - interval
    max = converted_amount + interval
    valid_answers = [min, max]
    user_guess = get_guess_from_user(rand_dollars)
    compare_results(user_guess, valid_answers,difficulty)


def get_guess_from_user(rand_dollars):
    user_input = input(f"Please guess the value of {rand_dollars} USD in ILS: ")
    user_guess = int(user_input)
    return user_guess


def play(difficulty):
    get_money_interval(difficulty)
