'''A module for demonstrating exceptions.'''

import sys
from math import log


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
        pass
    return x


def convert_details(s):
    '''Convert to an integer.'''
    try:
        return int(s)
    except (ValueError, TypeError) as e:
        print("Conversion error: {}".format(str(e)), file=sys.stderr)
        return -1


def convert_raise(s):
    '''Convert to an integer.'''
    try:
        return int(s)
    except(ValueError, TypeError) as e:
        print("Conversion error: {}".format(str(e)), file=sys.stderr)
        raise


def strong_log(s):
    v = convert_raise(s)
    return log(v)
