"""This function should return true if the seafood type is "mollusk" OR
it's been frozen for at least 7 days.
"""
def is_safe_to_eat(seafood_type, days_frozen):
    """
    >>> is_safe_to_eat("tuna", 3)
    False
    >>> is_safe_to_eat("salmon", 6)
    False
    >>> is_safe_to_eat("salmon", 7)
    True
    >>> is_safe_to_eat("mollusk", 1)
    True
    >>> is_safe_to_eat("mollusk", 9)
    True
    """
    if seafood_type=="mollusk" or days_frozen>=7:
        return True
    else:
        return False
print(is_safe_to_eat("mollusk",9))

