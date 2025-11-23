import math

def count_divisors(n):
    count = 0
    # Iterate from 1 up to the square root of n
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            # If i is a divisor, then n/i is also a divisor.
            # If i * i == n, then i and n/i are the same (e.g., for n=9, i=3, n/i=3).
            # In this case, we count it only once.
            if i * i == n:
                count += 1
            # Otherwise, i and n/i are distinct divisors, so we count both.
            else:
                count += 2
    return count
p=count_divisors(84)
print(p)
