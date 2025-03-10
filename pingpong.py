def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(8)
    8
    >>> pingpong(10)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    -2
    >>> pingpong(30)
    -2
    >>> pingpong(68)
    0
    >>> pingpong(69)
    -1
    >>> pingpong(80)
    0
    >>> pingpong(81)
    1
    >>> pingpong(82)
    0
    >>> pingpong(100)
    -6
    >>> from construct_check import check
    >>> # ban assignment statements
    >>> check(HW_SOURCE_FILE, 'pingpong',
    ...       ['Assign', 'AnnAssign', 'AugAssign', 'NamedExpr'])
    True
    """
    if n<8:
        return n
    k=0
    while inverse_helper(k)<n:
        k+=1
    if k%2==1:
        return pingpong(inverse_helper(k-1))+n-inverse_helper(k-1)
    else:
        return pingpong(inverse_helper(k-1))-n+inverse_helper(k-1)
    
def num_eights(pos):
    if pos%10==8:
        return 1
    elif pos<10:
        return 0
    return num_eights(pos//10)
def helper(n):#返回n以内含有8，或者被8整除的个数。
    k=1
    count=0
    while k<=n:
        if k%8==0 or num_eights(k)>0:
            count+=1
        k+=1
    return count
def inverse_helper(n):#helper的逆函数
    k=0
    while helper(k)<n:
        k+=1
    return k
print(pingpong(100))
print(pingpong(82))


