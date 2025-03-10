def num_eights(pos):
    """Returns the number of times 8 appears as a digit of pos.

    >>> num_eights(3)
    0
    >>> num_eights(8)
    1
    >>> num_eights(88888888)
    8
    >>> num_eights(2638)
    1
    >>> num_eights(86380)
    2
    >>> num_eights(12345)
    0
    >>> from construct_check import check
    >>> # ban all assignment statements
    >>> check(HW_SOURCE_FILE, 'num_eights',
    ...       ['Assign', 'AnnAssign', 'AugAssign', 'NamedExpr'])
    """
    count=0
    if pos%10==8:
        count+=1
    elif pos<10:
        return count
    return count+num_eights(pos//10)

print(num_eights(88888888))
print(num_eights(2638))
print(num_eights(86380))
print(num_eights(12345))    
