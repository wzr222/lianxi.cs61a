def hailstone(n):
    """Print the hailstone sequence starting at n and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    >>> b = hailstone(1)
    1
    >>> b
    1
    """
    while n>1:
        print(n)
        n=n//2 if n%2==0 else 3*n+1
        """if n%2==0:
            n//=2
        else:
            n=3*n+1
            这是上面的非简写形式"""
    return n
print(hailstone(27))
