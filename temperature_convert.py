"""
How can we communicate the highs and lows of climate change with people who use a different temperature unit? 
Let's make a temperature converter based on the steps here: 
https://www.mathsisfun.com/temperature-conversion.html

Create a function called celsius_to_fahrenheit that:
* takes a single argument, the temperature in celsius
* calculates and returns the fahrenheit equivalent

Similarly, create another function called fahrenheiht_to_celsius that:
* takes a single argument, the temperature in fahrenheit
* calculates and returns the celsius equivalent
"""

# This def statement may be incomplete...
def celsius_to_fahrenheit(celsius):
    """
    >>> celsius_to_fahrenheit(0)
    32
    >>> celsius_to_fahrenheit(100)
    212
    """
    return 32+1.8*celsius       
    
# This def statement may be incomplete...
def fahrenheit_to_celsius(fahrenheit):
    """
    >>> fahrenheit_to_celsius(32)
    0
    >>> fahrenheit_to_celsius(212)
    100
    """
    return (fahrenheit-32)/1.8
    
print(celsius_to_fahrenheit(0),fahrenheit_to_celsius(32))
