import os


def clear():
    """ Clears console
    :return:
    """
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')