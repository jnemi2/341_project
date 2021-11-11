from context import context
from enum import Enum


Status = Enum('Status', 'active playing standby pause inactive')


def initiate():
    """ Initiates the context of model
    """
    context.model.setdefault('status', Status.active)


def pause():
    """ Pauses the game and calls the pause menu function
    """
