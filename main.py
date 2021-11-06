import typespeed.menu

game = typespeed.menu.start()

rules = {'easy': {'time': 5, 'errors': 5, 'case_insensitive': True},
             'normal': {'time': 5, 'errors': 3, 'case_insensitive': True},
             'hard': {'time': 5, 'errors': 3, 'case_insensitive': False}}