global model  # type: dict
global view  # type: dict


def initiate():
    """ Initiates the global variables of the MVC context
    """
    global model
    global view
    model = dict()
    view = dict()


def set_model(new_model):
    global model
    model = new_model


def set_view(new_view):
    global view
    view = new_view
