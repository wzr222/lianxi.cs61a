def reverse(n):
    """Returns N with the digits reversed.
    >>> reverse_digits(123)
    321
    """
    n=str(n)
    if len(n)==1:
        return n
    else:
        return reverse(n[1:])+n[0]
print(reverse(123))

