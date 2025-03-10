"""
You know how old a dog is in human years, but what about dog years? Calculate it!

Write a function named calculate_dog_age that:
* takes 1 argument: a dog's age in human years.
* calculates the dog's age based on the conversion rate of 1 human year to 7 dog years.
* returns the age in dog years.
"""
def calculate_dog_age(years):
    """
    >>> calculate_dog_age(1)
    7
    >>> calculate_dog_age(0.5)
    3.5
    >>> calculate_dog_age(12)
    84
    """
    return 7*years
    
print(calculate_dog_age(8))