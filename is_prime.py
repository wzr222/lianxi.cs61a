def is_prime(n):
    """Returns True if n is a prime number and False otherwise.

    >>> is_prime(2)
    True
    >>> is_prime(16)
    False
    >>> is_prime(521)
    True
    """
    def f(n,k):
        if k==1:
            return True
        elif n%k==0:
            return False
        else:
            return f(n,k-1)
    return f(n,n-1)
print(is_prime(2))
print(is_prime(16))
print(is_prime(521))
"""
或者def helper f(k):
        if k>n**(0.5):
            return True
        elif n%k==0:
            retrurn False
        else:
            return f(k+1)
    return f(2)
"""

