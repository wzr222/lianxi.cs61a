def skip_mul(n):
    """Return the product of n * (n - 2) * (n - 4) * ...

    >>> skip_mul(5) # 5 * 3 * 1
    15
    >>> skip_mul(8) # 8 * 6 * 4 * 2
    384
    """
    if n == 2:
        return 2
    elif n==1:
        return 1
    else:
        return n * skip_mul(n - 2)
print(skip_mul(5))
print(skip_mul(8))

