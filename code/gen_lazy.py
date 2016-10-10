def take(count, iterable):
    counter = 0
    for item in iterable:
        if counter == count:
            return
        counter += 1
        yield item


def lucas():
    yield 2
    a = 2
    b = 1
    while True:
        yield b
        # update a and b to hold the new previous two values (uses tuple unpacking)
        a, b = b, a + b


def run_lucas():
    # the lucas generator can be used like any other iterable object
    for x in take(20, lucas()):
        print(x)

if __name__ == '__main__':
    run_lucas()
