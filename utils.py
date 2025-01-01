import os
import time

SCORES_FILE_NAME="Scores.txt"
BAD_RETURN_CODE = 666

def screen_cleaner(sleep_time):
    time.sleep(sleep_time)
    if os.getenv('TERM'):
        os.system('clear')
    else:
        print("\n" * 100)