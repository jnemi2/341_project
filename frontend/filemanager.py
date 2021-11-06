import pickle


def save_pkl(obj, file_name):
    """ Saves the game configuration
    :param obj: object to save in binary file with pickle
    :param file_name: str indicating filename including .pkl extension
    """
    file = open(file_name, "wb")
    pickle.dump(obj, file)
    file.close()


def load_pkl(file_name):
    """ Loads the game configuration
    :param file_name: str indicating filename including .pkl extension
    :return: dictionary with game configuration
    """
    file = open(file_name, "rb")
    obj = pickle.load(file)
    file.close()
    return obj
