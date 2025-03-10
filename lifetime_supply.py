"""
Ever wonder how much a "lifetime supply" of your favorite snack is? Wonder no more!

Write a function named calculate_supply that:
* takes 2 arguments: age, amount per day.
* calculates the amount consumed for rest of the life (based on a constant max age of 81).
* returns the result
"""

# This def statement may be incomplete...
def calculate_supply(age,amount_per_day):
    """
    >>> calculate_supply(80, 1)
    365
    >>> calculate_supply(80, 2)
    730
    >>> calculate_supply(36, 3)
    49275
    # Bonus: Accept floating point values for amount per day, and round the result up to an integer.
    >>> calculate_supply(37, 2.17)
    34850
    """
    return (81-age)*amount_per_day*365
    
print(calculate_supply(36,3))