def my_map(fn, seq):
    """Applies fn onto each element in seq and returns a list.
    >>> my_map(lambda x: x*x, [1, 2, 3])
    [1, 4, 9]
    """
    return [fn(x) for x in seq]
print(my_map(lambda x: x*x, [1, 2, 3]))

