"""
import typespeed.menu

game = typespeed.menu.start()
"""

from typespeed import model, menu
from context import context
from frontend import view

context.initiate()
view.initiate()
model.initiate()

menu.start()

print(context.view, context.model)
