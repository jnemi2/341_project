import os


def clear():
    """ Clears console
    :return:
    """
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def select(message, options, numerate=True):
    """ Requests and validates the choice of the user
    :param message: string to display
    :param options: list of strings with options (lowercase)
    :param numerate: if True, the validation will consider the index of the selection
                     if False, the validation will match a the user's input with an option
    :return: A string matching an option in 'options'
    """
    print(message)
    n_options = []
    # displaying options
    if numerate:
        for i in range(len(options)):
            print(str(i+1) + "- " + options[i])
            n_options.append(str(i+1))
    else:
        for i in options:
            print("- " + i)
    selection = input(">>").lower()
    # validation
    while selection not in options and (not numerate or (selection not in n_options)):
        selection = input("Please, enter a valid option>>").lower()
    # returning a valid option
    if selection not in options:
        return options[int(selection) - 1]
    return selection


def load_players(n_players):
    """ Generates a dictionary of players

    :param n_players: number of players to create
    :return: dictionary of players
    """
    return None

def start():
    """ Game configuration menu

    :return: dictionary with game parameters
    """
    config = {'mode': "default", 'difficulty': "normal",
              'players': []}
    clear()
    # print("Please, type the number of players")
    n_players = int(select("Please, select the number of players.",
                       ["2", "3", "4"], numerate=False))
    # load players
    return None
