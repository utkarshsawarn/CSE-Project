import math

def is_pronic(n):
    
    if n < 0:
        return False  # Pronic numbers are typically defined for non-negative integers

    for i in range(int(math.sqrt(n)) + 2): # Add 2 to ensure we check i*(i+1) where i is sqrt(n)
        if i * (i + 1) == n:
            return True
        elif i * (i + 1) > n:
            # If the product exceeds n, further iterations will also exceed n
            return False
    return False
print(is_pronic(66565))
print(is_pronic(7869))
print(is_pronic(5623))
