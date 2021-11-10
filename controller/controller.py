import context.context as context
import model.model as model
import view.view as view
from enum import Enum

Status = Enum('Status', 'active requested inactive')


def initiate():
    context.initiate()
    context.controller.setdefault('status', Status.active)
    model.initiate()
    view.initiate()


def test():
    print("stat model:", model.stat)
