from context import context
import msvcrt

CHARSET = "abcdefghijklmnopqrstuvwxyz 0123456789-?'<>`~!@#$%^&*+()_-=.,;:"
ENTER = '\\r'
BACK_SPACE = '\\x08'
ESC = '\\x1b'


def get_key():
    """ Returns the code of the current pressed key or ''
    :return: str of pressed key
    """
    if msvcrt.kbhit():
        return str(msvcrt.getch())[2:-1]  # returns the last pressed key
    else:
        return ''
