import utils


def add_score(difficulty):
    my_file = open(utils.SCORES_FILE_NAME, mode='w+')
    if (str(difficulty) == str(utils.BAD_RETURN_CODE)):
        my_file.write(str(difficulty))
    else:
        POINTS_OF_WINNING = str((difficulty*3 + 5))
        my_file.write(POINTS_OF_WINNING)

    lines = my_file.readline()
    for line in lines:
        print(line)
    my_file.close()