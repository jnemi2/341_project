

def new_stats():
    """ Generates a dictionary with stats
    :rtype: dictionary
    :return: dictionary with stats
    """
    return {'score': 0, 'mistakes': 0}


def new_player(name):
    """ Generates a dictionary with player information
    :param name: name of player
    :rtype: dictionary
    :return: dictionary with player information
    """
    return {'name': name, 'type': "human", 'stats': new_stats()}


def format_player(player):
    """ Formats a string with player information
    :param player: dictionary with player information
    :rtype: string
    :return: formatted string with player information
    """
    return "{} ({})".format(player['name'], player['type'])


def new_bot(name, accuracy):
    """ Generates a dictionary with bot information
    :param name: name of bot
    :param accuracy: float representing accuracy
    :rtype: dictionary
    :return: dictionary with bot  information
    """
    return {'name': name, 'type': "bot", 'accuracy': accuracy, 'stats': new_stats()}
