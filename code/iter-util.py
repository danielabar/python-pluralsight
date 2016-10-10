def first(iterable):
    """Return first item in series or raises a ValueError if series is empty"""
    iterator = iter(iterable)
    try:
        return next(iterator)
    except StopIteration:
        raise ValueError("iterable is empty")

print(first(['first', 'second', 'third']))

first(set())
