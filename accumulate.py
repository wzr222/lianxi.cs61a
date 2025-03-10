from operator import add, mul

square = lambda x: x * x

identity = lambda x: x

triple = lambda x: 3 * x

increment = lambda x: x + 1
def accumulate(merger, start, n, term):
    """Return the result of merging the first n terms in a sequence and start.
    The terms to be merged are term(1), term(2), ..., term(n). merger is a
    two-argument commutative function.

    >>> accumulate(add, 0, 5, identity)  # 0 + 1 + 2 + 3 + 4 + 5
    15
    >>> accumulate(add, 11, 5, identity) # 11 + 1 + 2 + 3 + 4 + 5
    26
    >>> accumulate(add, 11, 0, identity) # 11
    11
    >>> accumulate(add, 11, 3, square)   # 11 + 1^2 + 2^2 + 3^2
    25
    >>> accumulate(mul, 2, 3, square)    # 2 * 1^2 * 2^2 * 3^2
    72
    >>> # 2 + (1^2 + 1) + (2^2 + 1) + (3^2 + 1)
    >>> accumulate(lambda x, y: x + y + 1, 2, 3, square)
    19
    >>> # ((2 * 1^2 * 2) * 2^2 * 2) * 3^2 * 2
    >>> accumulate(lambda x, y: 2 * x * y, 2, 3, square)
    576
    >>> accumulate(lambda x, y: (x + y) % 17, 19, 20, square)
    16
    """
    k=1
    while k<=n:
        start=merger(start,term(k))
        k+=1
    return start
"""# Alternative solution
def accumulate_reverse(merger, start, n, term):
    total, k = start, n
    while k >= 1:
        total, k = merger(total, term(k)), k - 1
    return total

# Recursive solution
def accumulate2(merger, start, n, term):
    if n == 0:
        return start
    return merger(term(n), accumulate2(merger, start, n-1, term))
    
# Alternative recursive solution using start to keep track of total
def accumulate3(merger, start, n, term):
    if n == 0:
        return start
    return accumulate3(merger, merger(start, term(n)), n-1, term)
    """
print(accumulate(lambda x, y: (x + y) % 17, 19, 20, square))    
