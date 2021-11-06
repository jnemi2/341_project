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


def load_txt(file_name):
    """ Loads an entire .txt file of contiguous characters
    :param file_name: str name of file including .txt extension
    :return: list of lines of txt file
    """
    file = open(file_name, 'rt')
    line = file.readline()
    aux = list()
    while line is not None and line.strip() != "":
        aux.append(line.strip())
        line = file.readline()
    file.close()
    return aux
