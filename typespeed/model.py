from context import context
from typespeed import triggers
from enum import Enum


Status = Enum('Status', 'active playing standby pause inactive')


def initiate():
    """ Initiates the context of model
    """
    context.model.setdefault('status', Status.active)


def pause():
    """ Pauses the game and calls the pause menu function
    """


def request():
    """ Updates the status and calls triggers.request(), emulating input()
    :return: str with user input
    """
    prev_stat = context.model['status']
    context.model['status'] = Status.standby
    text = triggers.request()
    context.model['status'] = prev_stat
    return text
