import os


def clear():
    """ Clears console
    :return:
    """
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def display(message, end="\n", flush=False, bold=False):
    """ Displays a message
    :param message: str to display
    :param end: str added after message (default: '\n')
    :param flush: bool indicating whether or not to flush buffer
    :param bold: bool indicating whether message should be displayed in bold
    """
    if bold:
        message = '\033[1m' + message + '\033[0m'
    print(message, end=end, flush=flush)


def request():
    """ Requests an action from the user
    :return: str with information received by the user
    """
    return input(">>")
