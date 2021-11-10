import context.context as context
import controller.controller as controller
from enum import Enum

Status = Enum('Status', 'active standby inactive')


def initiate():
    """ Initiates context of model
    """
    context.model.setdefault('status', Status.active)


