def is_prime(n):
    """Return True iff N is prime."""
    k=2
    while k<n:
        if n%k==0:
            return "False"
        k+=1
    return "True"


def smallest_factor(n):
    """Returns the smallest value k>1 that evenly divides N."""
    k=2
    while k<n:
        if n%k==0:
            return k
        k+=1

def print_factors(n):
    """Print the prime factors of N."""
    k=2
    while k<=n:
        if n%k==0:
            print(k,end=",")
        k+=1

print(is_prime(7))
print(smallest_factor(99))
print_factors(99)