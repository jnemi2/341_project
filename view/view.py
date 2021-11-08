import os
from enum import Enum


Status = Enum('Status', 'active inactive')


def new_screen(context):
    """ Creates a new screen
    :param context: dict with context of MVC
    :return:
    """
    context['view']['screens'].append("")
    clear()


def back_screen(context):
    """ Deletes the current screen and displays the previous one
    :param context: dict with context of MVC
    :return:
    """
    screens = context['view']['screens']
    if len(screens) >= 2:
        screens.pop()
        display(screens[-1])


def update_screen(context, text):
    """ Updates a screen that is being displayed
    :param context: dict with context of MVC
    :param text: str to be displayed in the current screen
    :return:
    """
    screens = context['view']['screens']
    if len(screens) >= 1:
        screens[-1] = text
        clear()
        display(text)


def init_context():
    """ Creates a dictionary with context parameters for this module
    :return: dict with view context
    """
    aux = dict()
    aux.setdefault('status', Status.active)
    aux.setdefault('screens', list(" "))
    return aux


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
