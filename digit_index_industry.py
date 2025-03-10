def digit_index_factory(num, k):
    """
    Returns a function that takes no arguments, and outputs the offset
    between k and the rightmost digit of num. If k is not in num, then
    the returned function returns -1. Note that 0 is considered to
    contain no digits (not even 0).
    >>> digit_index_factory(34567, 4)() # .Case 1
    3
    >>> digit_index_factory(30001, 0)() # .Case 2
    1
    >>> digit_index_factory(999, 1)() # .Case 3
    -1
    >>> digit_index_factory(1234, 0)() # .Case 4
    -1
    """
    count = 0
    temp_num = num
    
    if num == 0:
        return lambda: -1
        
    while temp_num > 0:
        digit = temp_num % 10
        if digit == k:
            break
        count += 1
        temp_num //= 10
    
    def f():
        if temp_num == 0:  # k不在数字中
            return -1
        return count
    return f

# 测试代码
if __name__ == "__main__":
    # 测试用例
    print(digit_index_factory(120, 0)())  # 应该输出数字3在873211中从右边数的位置
