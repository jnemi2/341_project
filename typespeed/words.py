import frontend.filemanager as fm


def load_words(mode):
    """ Loads words from words module
    :param mode: a string specifying the game mode
    :rtype: tuple
    :return: a tuple containing 3 lists of loaded words by increasing length
    """
    if mode == "hard" or mode == "typespeed":
        return fm.load_txt("words1.txt"), fm.load_txt("words2.txt"), fm.load_txt("words3.txt")
    elif mode == "normal":
        return fm.load_txt("words1.txt"), fm.load_txt("words2.txt"), []
    else:
        return fm.load_txt("words1.txt"), [], []
