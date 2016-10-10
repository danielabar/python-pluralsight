"""Module for demonstrating generator execution."""


def take(count, iterable):
    """Take itemsm from teh front of an iterable.

    Args:
        count: The maximum number of items to retrieve.
        iterable: The source series.

    Yields:
        At most 'count' items from the 'iterable'.
    """
    # keep track of how many elements have been yielded so far
    counter = 0
    for item in iterable:
        if counter == count:
            # terminate stream of yielded values (raises StopIteration exception)
            return
        counter += 1
        print('.....take yield ' + str(item))
        yield item


def distinct(iterable):
    """Return unique items by eliminating duplicates.

    Args:
        iterable: The source series.

    Yields:
        Unique elements in order from 'iterable'.
    """
    # Use a set to keep track of what items we've already seen
    seen = set()
    for item in iterable:
        if item in seen:
            # Finish current iteration of loop and begin next iteration immediately
            continue
        print('.....distinct yield ' + str(item))
        yield item
        # When generator resumes, complete the work of the previous call by remembering what was seen
        # this works because 'item' is not re-assigned until we get back to for statement
        seen.add(item)


def run_distinct():
    print('=== DISTINCT ===')
    items = [5, 7, 7, 6, 5, 5]
    for item in distinct(items):
        print(item)


def run_take():
    print('=== TAKE ===')
    # create a source list for the generator function
    items = [2, 4, 6, 8, 10]
    for item in take(3, items):
        print(item)


def run_pipeline():
    print('=== PIPELINE ===')
    items = [3, 6, 6, 2, 1, 1]
    for item in take(3, distinct(items)):
        print(item)


if __name__ == '__main__':
    run_take()
    run_distinct()
    run_pipeline()
