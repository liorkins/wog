import os
import time
from random import randint

import score
import utils


def generate_sequence(list_size):
    rand_list = [randint(1,101) for _ in range(list_size)]
    print(f"Please try and remember following numbers: {rand_list} before hiding them in ...")
    utils.screen_cleaner(1)

    user_list=get_list_from_user(list_size)
    is_list_equal(rand_list,user_list,list_size)

def get_list_from_user(list_size):
    numbers = input(f"Enter {list_size} numbers separated by space: ").split()
    user_int_list = []
    if len(numbers)> list_size:
        print(f"Error! you entered invalid number of allowed numbers which is {list_size}")
    else:
        for num in numbers:
            user_int_list.append(int(num))
    return user_int_list


def is_list_equal(rand_list, usr_list,list_size):
   if rand_list == usr_list:
       print ("You made it! Lists are equal")
       score.add_score(list_size)
   else:
       score.add_score(utils.BAD_RETURN_CODE)
       print("Try again, lists are not equal")
def play(difficulty):
    generate_sequence(difficulty)