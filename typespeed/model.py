from context import context
from enum import Enum


Status = Enum('Status', 'active pause inactive')


def initiate():
    """ Initiates the context of model
    """
    context.model.setdefault('status', Status.active)
