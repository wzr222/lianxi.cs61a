def f(n):
    pre,aft=0,1
    k=1
    while (k<n):
        pre,aft=aft,pre+aft
        k+=1
    return aft
print(f(10))    
""" while语句是形如:while(condition):
                            body

"""
def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
print(fib(10))

assert fib(10)==f(10)
