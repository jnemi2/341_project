"""
import typespeed.menu

game = typespeed.menu.start()
"""
import controller.controller as controller
import context.context as context
import view.view as view


controller.initiate()  # Do not use any module of MVC before initiating

view.display("Hello ", bold=True, end='')
view.display("world!")
print(context.controller)
print(context.model)
print(context.view)
print("HELLO\x1b\x1b\x1b")
