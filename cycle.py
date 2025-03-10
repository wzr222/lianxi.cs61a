def compose(f,g):
    return lambda x:f(g(x))

def add1(x):
    return x + 1

def times2(x):
    return x * 2

def add3(x):
    return x + 3

def cycle(f1, f2, f3):
    """Returns a function that is itself a higher-order function."""
    def g(n):
        def h(x):
            if n == 0:
                return x
                
            result = x
            k = 1
            while k <= n:
                if k % 3 == 1:
                    result = f1(result)
                elif k % 3 == 2:
                    result = f2(result)
                else:
                    result = f3(result)
                k += 1
            return result
        return h
    return g

# 测试代码
if __name__ == "__main__":
    print(cycle(add1, times2, add3)(1)(5))  # 6
    print(cycle(add1, times2, add3)(2)(1))  # 4
    print(cycle(add1, times2, add3)(3)(2))  # 9
    print(cycle(add1, times2, add3)(4)(2))  # 10
    print(cycle(add1, times2, add3)(6)(1))  # 19
