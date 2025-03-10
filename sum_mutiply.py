""""
Write a function that sums up the multiples of a given number between a given start and end.
If the start or end numbers are also multiples, it should include them in the sum.

For example, if the range is 1-12 and the divisor is 4, the function should add 4+8+12, returning 24.
"""
def sum_multiples(start, end, divisor):
    """
    >>> sum_multiples(1, 12, 4)
    24
    >>> sum_multiples(1, 12, 13)
    0
    >>> sum_multiples(2, 2, 2)
    2
    >>> sum_multiples(2, 2, 3)
    0
    >>> sum_multiples(23, 81, 13)
    260
    """
    current=divisor 
    sum=0
    k=1    
    while(current<=end):
        if current>=start:
            sum+=current
        k+=1
        current = divisor*k
    return sum
print(sum_multiples(23,81,13))
