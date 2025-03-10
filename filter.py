def my_filter(pred, seq):
    """Keeps elements in seq only if they satisfy pred.
    >>> my_filter(lambda x: x % 2 == 0, [1, 2, 3, 4])  # new list has only even-valued elements
    [2, 4]
    """
    """ result = []
    for elem in seq:
        if pred(elem):
            result += [elem]
    return result"""
    return [x for x in seq if pred(x)]

print(my_filter(lambda x:x%2==0,[1,2,3,4,5]))
