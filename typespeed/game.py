import typespeed.words
import typespeed.menu
import time


def play(player, words, allowed_errors, typing_time, case_insensitive):
    """ Handles the logic behind each player's turn for the first game mode
    :param player: dictionary with player information
    :param words: tuple containing lists of loaded words
    :param allowed_errors: int indicating max errors allowed
    :param typing_time: int indicating max time (in seconds) per word
    :param case_insensitive: boolean indicating whether or not to normalize words
    """
    typespeed.menu.clear()
    print("Are you ready to start " + player['name'] + "?")
    typespeed.menu.select("Type ok to start", ["ok"], numerate=False)
    print("Ready")
    time.sleep(1.0)
    print("Set")
    time.sleep(1.0)
    print("Go!")
    time.sleep(1.0)
    typespeed.menu.clear()
    # logic


def play_typespeed(player, words):
    """ Handles the logic behing each player's turn for the typespeed mode
    :param player:
    :param words:
    :return:
    """
    # logic


def start(config):
    """ Starts a game with the specified configuration
    :param config: dictionary with game configuration
    """
    rules = {'easy': {'time': 5, 'errors': 5, 'case_insensitive': True},
             'normal': {'time': 5, 'errors': 3, 'case_insensitive': True},
             'hard': {'time': 5, 'errors': 3, 'case_insensitive': False}}
    print("Started game " + config['mode'])  # REMOVE
    mode = config['mode']
    words = typespeed.words.load_words(mode)
    for player in config['players']:
        play(player, words, rules[mode]['errors'], rules[mode]['time'], rules[mode]['case_insensitive'])
        # LOGIC AFTER EACH TURN
    # EVALUATE WINNER
