def front(s, f):
    """Return S but with elements chosen by F at the front.

    >>> front(range(10), lambda x: x % 2 == 1)  # odds in front
    [1, 3, 5, 7, 9, 0, 2, 4, 6, 8]
    """
    return [x for x in s if f(x)]+[x for x in s if not f(x)]
print(front(range(10), lambda x: x % 2 == 1))