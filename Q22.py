import sys
import time
start_time=time.time()

def sum_proper_divisors(n):
   
    if n <= 1:
        return 0  # No proper divisors for 0 or 1
    
    divisor_sum = 1  # 1 is always a proper divisor
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisor_sum += i
            if i != n // i:  # Avoid adding the same divisor twice for perfect squares
                divisor_sum += n // i
    return divisor_sum

def are_amicable(a, b):
    
    if a == b:  # Amicable numbers must be distinct
        return False
    
    sum_div_a = sum_proper_divisors(a)
    sum_div_b = sum_proper_divisors(b)
    
    return sum_div_a == b and sum_div_b == a
print(sum_proper_divisors(4))
print(are_amicable(65,78))
print(are_amicable(43,43))

print("---%s seconds ---"%(time.time() - start_time))
print(sys.getsizeof(sum_proper_divisors))
print(sys.getsizeof(are_amicable))
