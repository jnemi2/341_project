from frontend import filemanager, view
from typespeed import model
import typespeed.players as ply
import typespeed.game


max_players = 4
min_players = 2


def select(message, options, numerate=True):
    """ Requests and validates the choice of the user
    :param message: string to display
    :param options: list of strings with options (lowercase)
    :param numerate: if True, the validation will consider the index of the selection
                     if False, the validation will match a the user's input with an option
    :return: A string matching an option in 'options'
    """
    view.display(message)
    n_options = []
    # displaying options
    if numerate:
        for i in range(len(options)):
            view.display(str(i+1) + "- " + options[i])
            n_options.append(str(i+1))
    else:
        for i in options:
            view.display("- " + i)
    selection = model.request().strip().lower()
    # validation
    while selection not in options and (not numerate or (selection not in n_options)):
        view.display("Please, enter a valid option")
        selection = model.request().strip().lower()
    # returning a valid option
    if selection not in options:
        return options[int(selection) - 1]
    return selection


def pause():
    """ Opens the pause menu
    """
    # open new screen
    view.new_screen()
    view.display("Pause", bold=True, end='\n')
    selection = select("options:", ['back'])
    while selection != 'back':
        view.clear()
        selection = select("options:", ['back'])
    # close pause screen
    view.back_screen()


def add_player(players):
    """ Adds a new player to the list of players
    :param players: list of players
    """
    if len(players) < max_players:
        name = input("Enter player's name: ")
        player_type = select("Select player type:", ["human", "bot"])
        if player_type == "human":
            # new human
            players.append(ply.new_player(name))
        else:
            # new bot
            bot_accuracy = select("Select bot difficulty", ["easy", "smart", "hard"])
            if bot_accuracy == "easy":
                bot_accuracy = 0.65
            elif bot_accuracy == "smart":
                bot_accuracy = 0.75
            else:
                bot_accuracy = 0.85
            players.append(ply.new_bot(name, bot_accuracy))
    else:
        view.display("The maximum number of players has been reached.\n")


def display_players(players):
    """ Prints a list with player information
    :param players: list of players to display
    """
    for i in range(len(players)):
        view.display(str(i+1) + "- " + ply.format_player(players[i]))
    view.display("\n", end='', flush=True)


def remove_player(players):
    """ Removes a player from the list of players
    :param players: list of players
    """
    if len(players) > 0:
        display_players(players)
        to_remove = input("Please, select the index of the player you'd like to remove: ")
        try:
            players.pop(int(to_remove) - 1)
        except IndexError:
            view.display("Unable to remove player number " + to_remove)
        else:
            view.display("Player removed successfully.")
    else:
        view.display("There are no players.")


def edit_players(players):
    """ Generates a list of players
    :param players: list of players to edit
    :return: list of players
    """
    view.new_screen()
    selection = select("Options: ", ["list players", "add a player", "remove a player", "back"], numerate=True)
    while selection != "back":
        if selection == "list players":
            display_players(players)
        elif selection == "add a player":
            add_player(players)
        else:
            remove_player(players)
        selection = select("Options: ", ["list players", "add a player", "remove a player", "back"], numerate=True)
    view.back_screen()
    view.clear()


def config_game(config):
    """ Configures and starts a game with user parameters
    :param config: dictionary with game information
    """
    view.new_screen()
    print("New game")
    selection = select("Options: ", ["start", "edit players", "back"])
    while selection != "back":
        if selection == "edit players":
            edit_players(config['players'])
        else:
            if len(config['players']) < min_players:
                view.display("You cannot play with less than " + str(min_players) + " players.")
            else:
                config['mode'] = select("Select a game mode:", ["easy", "normal", "hard", "typespeed"])
                typespeed.game.start(config)
                break
        selection = select("Options: ", ["start", "edit players", "back"])
    view.back_screen()


def save(config):
    """ Asks the users if they'd like to save the game after each turn
    :param config: dictionary with the game configuration
    :return: boolean indicating whether the game was saved
    """
    selection = select("Would you like to save the game?", ["yes", "no"])
    if selection == "yes":
        filemanager.save_pkl(config, "game.pkl")
        return True
    return False


def resume():
    """ Loads the game configuration and resumes the game
    """
    try:
        config = filemanager.load_pkl("game.pkl")
    except FileNotFoundError:
        view.display("Unable to load file. Please, start a new game.")
    else:
        typespeed.game.start(config)


def start():
    """ Game menu
    """
    view.new_screen()
    config = {'mode': "normal", 'players': []}
    selection = select("Options: ", ["new game", "resume game", "exit"])
    while selection != "exit":
        if selection == "new game":
            config_game(config)
        else:
            resume()
        view.clear()
        selection = select("Options: ", ["new game", "resume game", "exit"])
    view.back_screen()
