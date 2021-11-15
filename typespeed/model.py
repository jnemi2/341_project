from context import context
from typespeed import triggers, menu
import datetime
from enum import Enum


Status = Enum('Status', 'active playing standby pause inactive')


def initiate():
    """ Initiates the context of model
    """
    context.model.setdefault('status', Status.active)
    context.model.setdefault('pause', False)
    context.model.setdefault('pause_time', datetime.timedelta(0))


def pause():
    """ Pauses the game and calls the pause menu function
    """
    if not context.model['pause'] and context.model['status'] == Status.standby:
        context.model['pause'] = True  # set pause status
        time_start = datetime.datetime.now()  # set pause time
        menu.pause()  # open pause menu
        context.model['pause_time'] = datetime.datetime.now() - time_start  # calculate pause time
        context.model['pause'] = False  # set standby status


def request():
    """ Updates the status and calls triggers.request(), emulating input()
    :return: str with user input
    """
    prev_stat = context.model['status']
    context.model['status'] = Status.standby
    text = triggers.request()
    context.model['status'] = prev_stat
    return text
