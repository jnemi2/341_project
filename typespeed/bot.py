import time
import random


def simulate(word, accuracy):
    """ Handles the logic behind the bots
    :param word: string to be typed by the bot
    :param accuracy: float indicating the bot's accuracy
    :return: word written with or without mistake
    """
    rnd = random.uniform(0, 1)
    if accuracy > rnd:
        # simulate correct input
        for c in word:
            print(c, end="", flush=True)
            time.sleep(0.2)
        print("")
    else:
        # simulate incorrect input
        mistake = random.randint(len(word)-1)
        word = word[:mistake-1] + word[mistake:]
        for c in word:
            print(c, end="", flush=True)
            time.sleep(0.2)
        print("")
    return word
