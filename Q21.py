import sys
import time
start_time=time.time()

def aliquot_sum(n):
    if not isinstance(n, int) or n <= 0:
        return "Input must be a positive integer."

    sum_of_divisors = 0
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            sum_of_divisors += i
    return sum_of_divisors

print(aliquot_sum(12))  # Output: 16 (1 + 2 + 3 + 4 + 6)
print(aliquot_sum(15))  # Output: 9  (1 + 3 + 5)
print(aliquot_sum(6))   # Output: 6  (1 + 2 + 3)
print(aliquot_sum(1))   # Output: 0

print("---%s seconds ---"%(time.time() - start_time))
print(sys.getsizeof(aliquot_sum))

