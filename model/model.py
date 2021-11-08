import typespeed.menu
from enum import Enum
import controller.controller as controller

Status = Enum('Status', 'active inactive standby working pause')


def init_context():
    """ Creates a dictionary with context parameters for this module
    :return: dictionary with model context
    """
    aux = dict()
    aux.setdefault('status', Status.active)
    # aux.setdefault('config', <CONFIG>)
    return aux


def update(context):
    """ Executes some model logic. This is called every iteration
    :param context: dict with MVC context
    :return:
    """
    # the instructions for each mode are called here
    stat = context['model']['status']
    if stat == Status.active:
        # active mode
        if context['key'] is not None and False:
            print(context['key'])
    elif stat == Status.standby:
        # standby mode
        if context['key'] is not None and False:
            print(context['key'])


def start(context):
    """ starts the module
    :param context: dict with MVC context
    :return:
    """
    controller.request(context)
