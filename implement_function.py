def remove(n, digit):
    """Return digits of non-negative N
    that are not DIGIT, for some
    non-negative DIGIT less than 10.
    >>> remove(231, 3)
    21
    >>> remove(243132, 2)
    4313
    """
    kept = 0
    digits = 0
    while n>0:
        last = n % 10
        n = n // 10
        if last!=digit:
            kept = kept + last*10**digits
            digits += 1
    return kept
print(remove(231,3))
print(remove(243132,2))
