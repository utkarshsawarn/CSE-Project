import sys
import time
start_time=time.time()

def is_deficient(n):
  if n <= 0:
    return False

  sum_of_proper_divisors = 0

  for i in range(1, n // 2 + 1):
    if n % i == 0:
      sum_of_proper_divisors += i

  return sum_of_proper_divisors < n

print(f"Is 8 deficient? {is_deficient(8)}")
print(f"Is 12 deficient? {is_deficient(12)}")
print(f"Is 21 deficient? {is_deficient(21)}")

print("---%s seconds ---"%(time.time() - start_time))
print(sys.getsizeof(is_deficient))
