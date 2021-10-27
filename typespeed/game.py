

def play(player, mode):
    """ Handles the logic behind each player's turn
    :param player: dictionary with player information
    :param mode: string containing game mode
    """


def start(config):
    """ Starts a game with the specified configuration
    :param config: dictionary with game configuration
    """
    print("Started game " + config['mode'])
    mode = config['mode']
    for player in config['players']:
        play(player, mode)
    # EVALUATE WINNER
