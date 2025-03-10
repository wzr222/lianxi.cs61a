from operator import add, mul, mod
def lambda_curry2(func):
    """
    Returns a Curried version of a two-argument function FUNC.
    >>> from operator import add, mul, mod
    >>> curried_add = lambda_curry2(add)
    >>> add_three = curried_add(3)
    >>> add_three(5)
    8
    >>> curried_mul = lambda_curry2(mul)
    >>> mul_5 = curried_mul(5)
    >>> mul_5(42)
    210
    >>> lambda_curry2(mod)(123)(10)
    3
    """
    def g(x):
        def h(y):
            return func(x,y)
        return h
    return g
print(lambda_curry2(add)(3)(5))
print(lambda_curry2(mul)(5)(42))
print(lambda_curry2(mod)(123)(10))

