""""
Implement a function that determines if a candidate can be president.
According to the US constitution, a presidential candidate must be at least 
35 years old and have been a US resident for at least 14 years. 
The age parameter represents a candidate's age and
the residency parameter represents their years of residency.
"""

def can_be_president(age, residency):
    """
    >>> can_be_president(30, 10)
    False
    >>> can_be_president(36, 10)
    False
    >>> can_be_president(30, 16)
    False
    >>> can_be_president(36, 15)
    True
    >>> can_be_president(36, 14)
    True
    >>> can_be_president(35, 14)
    True
    >>> can_be_president(35, 30)
    True
    """
    if age>=35 and residency>=14:
        return True
    else:
        return False
print(can_be_president(36,15))