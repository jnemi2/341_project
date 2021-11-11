"""
import typespeed.menu

game = typespeed.menu.start()
"""

from typespeed import model, menu, game
from context import context
from frontend import view

context.initiate()
view.initiate()
model.initiate()
