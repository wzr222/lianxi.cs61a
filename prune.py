def prune(d, keys):
    """Return a copy of D which only contains key/value pairs
    whose keys are also in KEYS.
    >>> prune({"a": 1, "b": 2, "c": 3, "d": 4}, ["a", "b", "c"])
    {'a': 1, 'b': 2, 'c': 3}
    """
    return {k:d[k] for k in keys }
print(prune({"a": 1, "b": 2, "c": 3, "d": 4}, ["a", "b", "c"]))
