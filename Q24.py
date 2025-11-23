import sys
import time
start_time=time.time()

import math

def count_divisors(num):
    divisor_count = 0
    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0:
            if num / i == i:
                divisor_count += 1
            else:
                divisor_count += 2
    return divisor_count

def is_highly_composite(n):
    """
    Checks if a number has more divisors than any smaller number.
    A number is highly composite if it has more divisors than any smaller number.
    """
    if n <= 0:
        return False

    original_divisors = count_divisors(n)
    # Check all numbers from n-1 down to 1
    for i in range(n - 1, 0, -1):
        if count_divisors(i) >= original_divisors:
            return False
    return True

# Example usage:
print(f"Is 12 highly composite? {is_highly_composite(12)}") # Expected: True
print(f"Is 10 highly composite? {is_highly_composite(10)}") # Expected: False
print(f"Is 1 highly composite? {is_highly_composite(1)}")   # Expected: True
print(f"Is 60 highly composite? {is_highly_composite(60)}") # Expected: True

print("---%s seconds ---"%(time.time() - start_time))
print(sys.getsizeof(count_divisors))
print(sys.getsizeof(is_highly_composite))

