
def count_until_larger(num):
    """
    Complete the function count_until_larger that takes in a positive integer num.
    count_until_larger examines the rightmost digit and counts digits from right to
    left until it encounters a digit larger than the rightmost digit, then returns that count.

    >>> count_until_larger(117) # .Case 1
    -1
    >>> count_until_larger(8117) # .Case 2
    3
    >>> count_until_larger(9118117) # .Case 3
    3
    >>> count_until_larger(8777)  # .Case 4
    3
    >>> count_until_larger(22) # .Case 5
    -1
    >>> count_until_larger(0) # .Case 6
    -1
    """
    m=0
    mid=num
    while mid>0:
        current=mid%10
        mid1=mid
        while mid1>0:
            k=mid1%10
            if k>current:
                m+=1
            k+=1
            mid1//=10
        mid//=10
    if m==0:
        return -1
    else:
        return m
print(count_until_larger(0))