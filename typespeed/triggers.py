from context import context
from frontend import view


def request():
    """ Reads an input from the user. Emulates input()
    :return: str with user input
    """
    key = ''
    while key != view.ENTER:
        # update key
        key = view.get_key()
        # check triggers
        trigger(key)
    # return input


def trigger(key):
    """ Handles the actions triggered by the keyboard
    :param key: str code of key pressed
    """
    if key != '':
        if key.lower() in view.CHARSET:
            view.display(key, flush=True)
        elif key == view.ENTER:  # new line
            view.display('\n', end='', flush=True)
        elif key == view.BACK_SPACE:  # backspace
            view.backspace()
        elif key == view.ESC:  # esc
            context.controller['status'] = Status.inactive  # pause