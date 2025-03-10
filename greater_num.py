"""
Write a function named greater_num that:
* takes 2 arguments, both numbers.
* returns whichever number is the greater (higher) number.
Use an if/else to implement the function.
"""
def greater_num(num1, num2):
    """
    >>> greater_num(45, 10)
    45
    >>> greater_num(-1, 30)
    30
    >>> greater_num(20, 20)
    20
    """
    if num1>num2:
        return num1
    else:
        return num2
print(greater_num(45,10))
