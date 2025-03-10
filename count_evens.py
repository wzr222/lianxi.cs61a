"""Write a function that will count the number of even numbers between a given start number and a given end number.
It should include the start or end if they are even.
"""
def count_evens(start, end):
    """
    >>> count_evens(2, 2)
    1
    >>> count_evens(-2, 52)
    28
    >>> count_evens(237, 500)
    132
    """
    if (end-start)%2==1:
        return (end-start+1)//2
    else:
        if start%2==0:
            return (end-start)//2+1
        else:
            return (end-start)//2
print(count_evens(237,500))
  
