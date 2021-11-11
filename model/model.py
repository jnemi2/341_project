import context.context as context
import controller.controller as controller
from typespeed import bot, game, menu, players, words
from enum import Enum

Status = Enum('Status', 'active standby inactive')


def initiate():
    """ Initiates context of model
    """
    context.model.setdefault('status', Status.active)


def start():
    print("Starting model")  # DELETE


def update():
    print("Updating")  # DELETE
