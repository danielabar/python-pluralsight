'''A module for demonstrating exceptions.'''


def convert(s):
    '''Convert to an integer.'''
    x = int(s)
    return x


def convert_handle(s):
    '''Convert to an integer.'''
    try:
        x = int(s)
        print("Conversion succeeded! x =", x)
    except ValueError:
        print("Conversion failed.")
        x = -1
    except TypeError:
        print("Conversion failed.")
        x = -1
    return x


def convert_collapse(s):
    '''Convert to an integer.'''
    x = -1
    try:
        x = int(s)
        print("Conversion succeeded! x =", x)
    except (ValueError, TypeError):
        print("Conversion failed.")
    return x
