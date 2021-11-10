global model  # type: dict
global view  # type: dict
global controller  # type: dict


def initiate():
    """ Initiates the global variables of the MVC context
    """
    global model
    global view
    global controller
    model = dict()
    view = dict()
    controller = dict()
