from context import context
from typespeed import game, model
from frontend import view


def request():
    """ Reads an input from the user. Emulates input()
    :return: str with user input
    """
    key = ''
    view.display('\n')
    while key != view.ENTER:
        # update key
        key = view.get_key()
        # check triggers
        trigger(key)
    # return last line in screen
    return context.view['screens'][-1].split('\n')[-1].strip()


def trigger(key):
    """ Handles the actions triggered by the keyboard
    :param key: str code of key pressed
    """
    if key != '':
        # select behaviour depending on status
        stat = context.model['status']
        if stat == model.Status.standby:
            # status defined behaviour
            if key.lower() in view.CHARSET:
                view.display(key, flush=True)
            elif key == view.ENTER:  # new line
                view.display('\n', end='', flush=True)
            elif key == view.BACK_SPACE:  # backspace
                view.backspace()
            elif key == view.ESC:  # esc
                model.pause()  # pause

