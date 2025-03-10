
def f(x):
    return g(x - 1)
    
def g(y):
    return abs(h(y) - h(1 / y))
    
def h(z):
    return z * z
    
print(f(12))