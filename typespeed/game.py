import typespeed.words
import typespeed.menu
import typespeed.players as ply
import time
import random
import datetime


def random_word(words):
    """ Selects a random word
    :param words: tuple containing 3 lists of words
    :return: string with one random word
    """
    aux = random.randint(1, 12)
    if len(words[2]) > 0:  # which means the game mode is either hard or typespeed
        if aux > 6:
            word = words[2][random.randint(0, len(words[2])-1)]
        elif aux > 2:
            word = words[1][random.randint(0, len(words[1])-1)]
        else:
            word = words[0][random.randint(0, len(words[0])-1)]
    elif len(words[1]) > 0:  # which means the game mode is normal
        if aux > 4:
            word = words[1][random.randint(0, len(words[1])-1)]
        else:
            word = words[0][random.randint(0, len(words[0])-1)]
    else:  # which means the game mode is easy
        word = words[0][random.randint(0, len(words[0])-1)]
    return word


def detect_input(word, case_insensitive):
    """ Compares user input with word and generates stats
    :param word: string to compare
    :param case_insensitive: boolean indicating whether the comparison is case insensitive
    :return: dictionary with statistics
    """
    stats = {}
    print('\033[1m' + word + '\033[0m')
    t0 = datetime.datetime.now()
    text = input(">>")
    stats.setdefault('time_diff', datetime.datetime.now() - t0)
    if case_insensitive:
        text = text.lower()
        word = word.lower()
    stats.setdefault('match', text.strip() == word)
    return stats


def confirm_start(name):
    """ Asks for confirmation to start
    :param name: name of player
    """
    typespeed.menu.select("Ready to start " + name + "?", ["ok"], numerate=False)
    print("Ready")
    time.sleep(1.0)
    print("Set")
    time.sleep(1.0)
    print("Go!")
    time.sleep(1.0)
    typespeed.menu.clear()


def play(player, words, allowed_errors, typing_time, case_insensitive):
    """ Handles the logic behind each player's turn for the first game mode
    :param player: dictionary with player information
    :param words: tuple containing lists of loaded words
    :param allowed_errors: int indicating max errors allowed
    :param typing_time: int indicating max time (in seconds) per word
    :param case_insensitive: boolean indicating whether or not to normalize words
    """
    typespeed.menu.clear()
    print("You'll have " + str(typing_time) + " seconds to type each word.")
    confirm_start(player['name'])
    # game logic
    errors = player['stats']['errors']
    score = player['stats']['score']
    while errors < allowed_errors:
        word = random_word(words).strip()
        stats = detect_input(word, case_insensitive)
        if (not stats['match']) or (stats['time_diff'] > datetime.timedelta(seconds=typing_time)):
            errors += 1
            print("Errors: ({}/{})".format(errors, allowed_errors))
        else:
            score += len(word)
            print("Score: {}".format(score))
    player['stats']['score'] = score
    player['stats']['errors'] = errors


def play_typespeed(player, words):
    """ Handles the logic behing each player's turn for the typespeed mode
    :param player:
    :param words:
    :return:
    """
    typespeed.menu.clear()
    print("")  # Explanation
    confirm_start(player['name'])
    errors = 0
    score = 0
    # game logic
    for i in range(15):
        word = random_word(words).strip()
        stats = detect_input(word, case_insensitive=False)
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
        # ask if user wants to save or continue
    # Winner? find player with the highest score
    winner = config['players'][0]
    for i in config['players']:
        if i['stats']['score'] > winner['stats']['score']:
            winner = i
            i['stats'] = ply.new_stats()
    typespeed.menu.clear()
    print("The winner is {}.".format(winner['name']))
