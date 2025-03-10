from operator import add, sub, mul, truediv, floordiv, mod

"""
In the console, type expressions that use function calls
and correspond to each arithmetic expression.
Use the console to check your work.

Useful documentation:
https://docs.python.org/3/library/operator.html#mapping-operators-to-functions
"""

# Q1: 30 + 2

# Q2: 30 - 2

# Q3: 30 * 2

# Q4: 30 / 2

# Q5: 30 % 2

# Nested!

# Q6: 30 + (2 * 4)

# Q7: 3 * (10 - 2)

# Challenge!

# Q8: (3 ** (365/52)) - 1

# Q9: (25 // 4) - (25 / 4)

print(add(2,30),sub(30,2),mul(30,2),floordiv(30,2),mod(30,2))
print(add(30,mul(2,4)),sub(pow(3,truediv(365,52)),1),sub(floordiv(25,4),truediv(25,4)))