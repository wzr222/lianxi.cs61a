def largest_factor(n):
    """Return the largest factor of n that is smaller than n.

    >>> largest_factor(15) # factors are 1, 3, 5
    5
    >>> largest_factor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
    40
    >>> largest_factor(13) # factor is 1 since 13 is prime
    1
    """
    k=0
    while(k<n):
        k+=1
        if n%k==0 and k<n:
            d=k
    if d==1:
        return "factor is 1 since {} is a prime".format(n)    
    else:
        return d
    """
    或者从上到下factor=n-1,
    while:
        factor>1
        if n%factor==0 :
            return factor
        else:
            factor-=1
    """
print(largest_factor(13))   
