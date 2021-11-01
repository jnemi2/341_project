import time
import random


def simulate(word, accuracy):
    """ Handles the logic behind the bots
    :param word: string to be typed by the bot
    :param accuracy: float indicating the bot's accuracy
    """
    rnd = random.uniform(0, 1)
    if accuracy > rnd:
        # correct
        for c in word:
            print(c, end="")
            time.sleep(0.25)
        print("")
    else:
        # incorrect
        mistake = random.randint(len(word)-1)
        word = word[:mistake-1] + word[mistake:]
        for c in word:
            print(c, end="")
            time.sleep(0.25)
        print("")
