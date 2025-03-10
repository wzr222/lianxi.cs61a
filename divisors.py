def divisors(n):
    """Returns all the divisors of N.

    >>> divisors(12)
    [1, 2, 3, 4, 6]
    """
    return [k for k in range(1,n) if n%k==0]
print(divisors(12))