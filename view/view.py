import context.context as context
import msvcrt
import os
from enum import Enum

Status = Enum('Status', 'active inactive requested')


def initiate():
    """ Initiates the context of view
    """
    context.view.setdefault('status', Status.active)
    context.view.setdefault('screens', list())
    context.view.setdefault('key', "")


def clear():
    """ Clears console
    """
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def new_screen(text=""):
    """ Appends a new screen
    """
    context.view['screens'].append(text)
    clear()


def display(text, end='', bold=False, flush=False):
    """ Adds content to the current screen
    :param text: str to be displayed
    :param end: str to append to text
    :param bold: bool indicating whether the text should be styled as bold
    :param flush: bool indicating whether the buffer is to be freed immediately
    """
    screens = context.view['screens']
    if bold:
        aux = '\033[1m' + text + '\033[0m' + end
    else:
        aux = text + end
    if len(screens) < 1:
        new_screen(aux)  # creates a new screen if none had been created
    else:
        screens[-1] = screens[-1] + aux  # adds content to screen
    print(aux, end=end, flush=flush)


def backspace(can_delete_line=False):
    """ Deletes the last character on the current screen
    :param can_delete_line: bool indicating whether it is possible to delete a '\n'
    """
    screens = context.view['screens']
    if len(screens) > 0:
        if can_delete_line or screens[-1][-1] != '\n':
            aux = screens[-1][:-1]
            screens[-1] = aux
            clear()
            print(aux, end='', flush=True)


def update_screen(text):
    """ Updates the content of a screen
    """
    screens = context.view['screens']
    if len(screens) < 1:
        new_screen(text)  # creates a new screen if none had been created
    else:
        screens[-1] = text  # updates the screen
        clear()
        print(text, end='', flush=True)


def get_key():
    """ Returns the code of the current pressed key or ''
    :return: str of pressed key
    """
    if msvcrt.kbhit():
        return str(msvcrt.getch())[2:-1]  # returns the last pressed key
    else:
        return ''
