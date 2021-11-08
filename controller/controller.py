import msvcrt
from enum import Enum
import model.model as model
import view.view as view

Status = Enum('Status', 'active inactive requested')


def request(context):
    """ handles a request of information from the user. Emulates input()
    :param context: dict with context information
    :return: str with user input
    """
    if context['controller']['status'] == Status.active:
        context['controller']['status'] = Status.requested
        view.update_screen(context, context['view']['screens'][-1] + "\n>> ")


def update(context):
    """ Updates every component
    :param context: dict with context information
    :return:
    """
    # update code
    model.update(context)

    # status active
    stat = context['controller']['status']
    if stat == Status.requested:
        # status requested
        key = context['key']
        if key is not None and key.lower() in "abcdefghijklmnopqrstuvwxyz -?'!@#$%^&*()_-=.,;:":
            buffer = context['controller']['buffer']
            buffer.append(key)
            view.update_screen(context, context['view']['screens'][-1] + key)


def start():
    """ Initiates the components and the loop
    """
    # Initiate Model and View
    status = Status.active
    context = {
        'controller': {'status': Status.active, 'buffer': list()},
        'model': model.init_context(),
        'view': view.init_context(),
        'key': None
    }  # context
    # start modules
    model.start(context)
    # start loop
    while status != Status.inactive:
        if msvcrt.kbhit():
            key_stroke = msvcrt.getch()
            context['key'] = str(key_stroke)[2:-1]  # will save which key is pressed
        else:
            context['key'] = None
        update(context)

