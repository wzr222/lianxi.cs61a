def flatten(s):
    """Returns a flattened version of list s.

    >>> flatten([1, 2, 3])     # normal list
    [1, 2, 3]
    >>> x = [1, [2, 3], 4]     # deep list
    >>> flatten(x)
    [1, 2, 3, 4]
    >>> x # Ensure x is not mutated
    [1, [2, 3], 4]
    >>> x = [[1, [1, 1]], 1, [1, 1]] # deep list
    >>> flatten(x)
    [1, 1, 1, 1, 1, 1]
    >>> x
    [[1, [1, 1]], 1, [1, 1]]
    """
    # 基本情况：空列表
    if not s:
        return []
        
    # 如果第一个元素是列表，递归展平它并与剩余部分的展平结果合并
    if isinstance(s[0], list):
        return flatten(s[0]) + flatten(s[1:])
    # 如果第一个元素不是列表，将其放入列表并与剩余部分的展平结果合并
    else:
        return [s[0]] + flatten(s[1:])

# 测试代码
if __name__ == "__main__":
    print(flatten([1, [2, 3], 4]))          # [1, 2, 3, 4]
    print(flatten([1, 2, 3]))               # [1, 2, 3]
    print(flatten([[1, [1, 1]], 1, [1, 1]]))# [1, 1, 1, 1, 1, 1]
