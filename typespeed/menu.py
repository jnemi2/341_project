import frontend.filemanager
import typespeed.players as ply
import typespeed.game
from frontend.view import clear, display

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
    display(message)
    n_options = []
    # displaying options
    if numerate:
        for i in range(len(options)):
            display(str(i+1) + "- " + options[i])
            n_options.append(str(i+1))
    else:
        for i in options:
            display("- " + i)
    selection = input(">>").strip().lower()
    # validation
    while selection not in options and (not numerate or (selection not in n_options)):
        selection = input("Please, enter a valid option>>").strip().lower()
    # returning a valid option
    if selection not in options:
        return options[int(selection) - 1]
    return selection


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
        display("The maximum number of players has been reached.\n")


def display_players(players):
    """ Prints a list with player information
    :param players: list of players to display
    """
    for i in range(len(players)):
        display(str(i+1) + "- " + ply.format_player(players[i]))
    display("\n")


def remove_player(players):
    """ Removes a player from the list of players
    :param players: list of players
    """
    if len(players) > 0:
        display_players(players)
        to_remove = input("Please, select the index of the player you'd like to remove: ")
        try:
            players.pop(int(to_remove) - 1)
        except:
            display("Unable to remove player number " + to_remove + ".\n")
        else:
            display("Player removed successfully.\n")
    else:
        display("There are no players.\n")


def edit_players(players):
    """ Generates a list of players
    :param players: list of players to edit
    :return: list of players
    """
    clear()
    selection = select("Options: ", ["list players", "add a player", "remove a player", "back"], numerate=True)
    while selection != "back":
        if selection == "list players":
            display_players(players)
        elif selection == "add a player":
            add_player(players)
        else:
            remove_player(players)
        selection = select("Options: ", ["list players", "add a player", "remove a player", "back"], numerate=True)


def config_game(config):
    """ Configures and starts a game with user parameters
    :param config: dictionary with game information
    """
    clear()
    print("New game")
    selection = select("Options: ", ["start", "edit players", "back"])
    while selection != "back":
        if selection == "edit players":
            edit_players(config['players'])
        else:
            if len(config['players']) < min_players:
                display("You cannot play with less than " + str(min_players) + " players.")
            else:
                config['mode'] = select("Select a game mode:", ["easy", "normal", "hard", "typespeed"])
                typespeed.game.start(config)
                break
        selection = select("Options: ", ["start", "edit players", "back"])


def save(config):
    """ Asks the users if they'd like to save the game after each turn
    :param config: dictionary with the game configuration
    :return: boolean indicating whether the game was saved
    """
    selection = select("Would you like to save the game?", ["yes", "no"])
    if selection == "yes":
        frontend.filemanager.save_pkl(config, "game.pkl")
        return True
    return False


def resume():
    """ Loads the game configuration and resumes the game
    """
    try:
        config = frontend.filemanager.load_pkl("game.pkl")
        typespeed.game.start(config)
    except:
        display("Unable to load file. Please, start a new game.")


def start():
    """ Game menu
    """
    config = {'mode': "normal", 'players': []}
    selection = select("Options: ", ["new game", "resume game", "exit"])
    while selection != "exit":
        if selection == "new game":
            config_game(config)
        else:
            resume()
        selection = select("Options: ", ["new game", "resume game", "exit"])
