'''A module for demonstrating exceptions.'''


def convert(s):
    '''Convert to an integer.'''
    x = int(s)
    return x


def convert_handle(s):
    '''Convert to an integer.'''
    try:
        x = int(s)
    except ValueError:
        x = -1
    return x
