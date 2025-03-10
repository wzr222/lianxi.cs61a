def merge(n1, n2):
    """ Merges two numbers by digit in decreasing order
    >>> merge(31, 42)
    4321
    >>> merge(21, 0)
    21
    >>> merge(21, 31) 
    3211
    >>> merge(32231, 42)
    43221
    """
    def count_digits(n):
        # 统计数字中每个数字出现的次数
        counts = {}
        while n > 0:
            digit = n % 10
            counts[digit] = counts.get(digit, 0) + 1
            n //= 10
        return counts
    
    # 基本情况
    if n1 == 0:
        return n2
    if n2 == 0:
        return n1
        
    # 获取两个数字的所有数字及其出现次数
    counts1 = count_digits(n1)
    counts2 = count_digits(n2)
    
    # 合并两个计数字典
    all_counts = {}
    for d in counts1:
        all_counts[d] = counts1[d]
    for d in counts2:
        all_counts[d] = all_counts.get(d, 0) + counts2[d]
    
    # 构建结果
    result = 0
    for digit in range(9, -1, -1):  # 从9到0
        if digit in all_counts:
            for _ in range(all_counts[digit]):
                result = result * 10 + digit
                
    return result

# 测试代码
if __name__ == "__main__":
    print(merge(32231, 42))    # 43221
    print(merge(21, 0))        # 21
    print(merge(21, 31))       # 3211
    print(merge(753, 862))     # 87632
    print(merge(15, 93))       # 9531