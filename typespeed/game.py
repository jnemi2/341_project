import typespeed.words
import typespeed.menu
import typespeed.players as ply
import typespeed.bot
from typespeed import model
import time
import random
import datetime

from frontend.filemanager import load_pkl
from frontend.view import clear, display
from context import context


def pause():
    """ Pauses the game and opens the pause menu
    """


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


def levenshtein_distance(first_word: str, second_word: str) -> int:
    """Implementation of the levenshtein distance in Python.
    :param first_word: the first word to measure the difference.
    :param second_word: the second word to measure the difference.
    :return: the levenshtein distance between the two words.
    Examples:
    levenshtein_distance("planet", "planetary")
    3
    levenshtein_distance("", "test")
    4
    levenshtein_distance("book", "back")
    2
    levenshtein_distance("book", "book")
    0
    levenshtein_distance("test", "")
    4
    levenshtein_distance("", "")
    0
    levenshtein_distance("orchestration", "container")
    10
    """
    # The longer word should come first
    if len(first_word) < len(second_word):
        return levenshtein_distance(second_word, first_word)
    if len(second_word) == 0:
        return len(first_word)
    previous_row = range(len(second_word) + 1)
    for i, c1 in enumerate(first_word):
        current_row = [i + 1]
        for j, c2 in enumerate(second_word):
            # Calculate insertions, deletions and substitutions
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1
            substitutions = previous_row[j] + (c1 != c2)
            # Get the minimum to append to the current row
            current_row.append(min(insertions, deletions, substitutions))
        # Store the previous row
        previous_row = current_row
    # Returns the last element (distance)
    return previous_row[-1]


def detect_input(word, case_insensitive, simulate=False, accuracy=1.0):
    """ Compares user input with word and generates stats
    :param word: string to compare
    :param case_insensitive: boolean indicating whether the comparison is case insensitive
    :param simulate: simulates an input with a certain accuracy
    :param accuracy: typing accuracy of simulation
    :return: dictionary with statistics
    """
    stats = {}
    display(word, bold=True)
    t0 = datetime.datetime.now()
    if not simulate:
        text = model.request()
    else:
        text = typespeed.bot.simulate(word, accuracy)
    stats.setdefault('time_diff', datetime.datetime.now() - t0 - context.model['pause_time'])
    context.model['pause_time'] = datetime.timedelta(0)  # resets pause time
    if case_insensitive:
        text = text.lower()
        word = word.lower()
    stats.setdefault('match', levenshtein_distance(text.strip(), word))
    return stats


def confirm_start(name):
    """ Asks for confirmation to start
    :param name: name of player
    """
    typespeed.menu.select("Ready to start " + name + "?", ["ok"], numerate=False)
    display("Ready")
    time.sleep(1.0)
    display("Set")
    time.sleep(1.0)
    display("Go!")
    time.sleep(1.0)
    clear()


def play(player, words, rules):
    """ Handles the logic behind each player's turn for the first game mode
    :param player: dictionary with player information
    :param words: tuple containing lists of loaded words
    :param rules: dict with rules for the specified game mode
    """
    clear()
    message = "You'll have " + str(rules['time']) + " seconds to type each word. Case "
    if rules['case_insensitive']:
        message = message + "insensitive."
    else:
        message = message + "sensitive."
    display(message, bold=True)
    confirm_start(player['name'])
    # game logic
    errors = 0
    score = 0
    while errors < rules['errors']:
        clear()
        word = random_word(words).strip()
        display("Errors: ({}/{}) | Score: {}".format(errors, rules['errors'], score))
        if player['type'] == "bot":
            stats = detect_input(word, rules['case_insensitive'], simulate=True, accuracy=player['accuracy'])
        else:
            stats = detect_input(word, rules['case_insensitive'])
        if (stats['match'] != 0) or (stats['time_diff'] > datetime.timedelta(seconds=rules['time'])):
            errors += 1
        else:
            score += len(word)
    player['stats']['score'] = score
    player['stats']['errors'] = errors


def play_typespeed(player, words):
    """ Handles the logic behing each player's turn for the typespeed mode
    :param player:
    :param words:
    :return:
    """
    clear()
    # Explanation
    display("You will be shown 15 words that you will need to type in the shortest possible time.", bold=True)
    confirm_start(player['name'])
    word_distance = 0
    total_time = datetime.timedelta(seconds=0)
    words_len = 0
    # game logic
    for i in range(15):
        clear()
        word = random_word(words).strip()
        if player['type'] == "bot":
            stats = detect_input(word, case_insensitive=False, simulate=True, accuracy=player['accuracy'])
        else:
            stats = detect_input(word, case_insensitive=False)
        word_distance += stats['match']
        words_len += len(word)
        total_time = total_time + stats['time_diff']
    player['stats']['score'] = 100 / ((word_distance / words_len) + (total_time.seconds / words_len))
    player['stats']['errors'] = 1  # this will be used as an indicator


def show_ranking(players):
    """ Displays the list of players sorted by score
    :param players: list of players
    """
    aux = players[:]
    aux.sort(key=lambda x: int(round(x['stats']['score'])), reverse=True)
    for p in range(len(aux)):
        display("{}?? {} ({})".format(p+1, aux[p]['name'], round(aux[p]['stats']['score'], 2)))
    display("\nPress enter to continue.", end='\n', flush=True)
    model.request()


def start(config):
    """ Starts a game with the specified configuration
    :param config: dictionary with game configuration
    """
    context.model['pause_time'] = datetime.timedelta(0)  # reset pause time
    rules = load_pkl("params.pkl")
    mode = config['mode']
    words = typespeed.words.load_words(mode)
    for i in range(len(config['players'])):
        player = config['players'][i]
        if player['stats']['errors'] == 0:
            context.model['status'] = model.Status.playing
            if mode != "typespeed":
                play(player, words, rules[mode])
            else:
                play_typespeed(player, words)
            # LOGIC AFTER EACH TURN
            context.model['status'] = model.Status.active
            saved = False
            if i < len(config['players'])-1:
                saved = typespeed.menu.save(config)
                if saved:
                    break
    clear()
    display("")
    if not saved:
        show_ranking(config['players'])
    display("")
    for player in config['players']:
        player['stats'] = ply.new_stats()
