import context.context as context
import model.model as model
import view.view as view
from enum import Enum

Status = Enum('Status', 'active reading inactive')


def initiate():
    """ Initiates the components of the MVC
    """
    context.initiate()
    context.controller.setdefault('status', Status.active)
    model.initiate()
    view.initiate()


def start():
    """ Starts the controller module
    """
    # start code goes here
    model.start()

    # starts a loop until controller is deactivated
    while context.controller['status'] != Status.inactive:
        update()


def update():
    """ This code is executed in a loop until the status of controller is set to inactive
    """
    # behaviour of controller
    key = view.get_key()
    if context.controller['status'] == Status.reading:
        trigger(key)  # calling keyboard triggers

    # Calls to functions from other components
    model.update()


def trigger(key):
    """ Handles the actions triggered by the keyboard
    :param key: str code of key pressed
    """
    if key != '':
        if key.lower() in "abcdefghijklmnopqrstuvwxyz 0123456789-?'<>`~!@#$%^&*+()_-=.,;:":
            view.display(key, flush=True)
        elif key == '\\r':  # new line
            view.display('\n', end='', flush=True)
        elif key == '\\x08':  # backspace
            view.backspace()
        elif key == '\\x1b':  # esc
            context.controller['status'] = Status.inactive
