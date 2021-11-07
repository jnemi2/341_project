import msvcrt
from enum import Enum
import model.model as model

Status = Enum('Status', 'active inactive required')


def update(context):
    """ Updates every component
    :param context: dict with context information
    :return:
    """
    print(model.Status.active)



def start():
    """ Initiates the components and the loop
    """
    # Initiate Model and View
    status = Status.active
    context = {}  # context
    while status != Status.inactive:
        if msvcrt.kbhit():
            key_stroke = msvcrt.getch()
            print(str(key_stroke)[2:-1])  # will print which key is pressed
        update(context)

