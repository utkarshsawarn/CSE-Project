import sys
import time
start_time=time.time()

def is_mersenne_prime(p):
   
    n = 2**p - 1
    if n <= 1:
        return False
    
    # Trial division to check for primality
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
            
    return True


# p=3, Mersenne number is 2^3 - 1 = 7, which is prime
print(f"Is 2^3 - 1 a Mersenne prime? {is_mersenne_prime(3)}")

# p=5, Mersenne number is 2^5 - 1 = 31, which is prime
print(f"Is 2^5 - 1 a Mersenne prime? {is_mersenne_prime(5)}")

# p=11, Mersenne number is 2^11 - 1 = 2047 = 23 * 89, not prime
print(f"Is 2^11 - 1 a Mersenne prime? {is_mersenne_prime(11)}")
print(f"Is 2^22 - 1 a Mersenne prime? {is_mersenne_prime(22)}")

print("---%s seconds ---"%(time.time() - start_time))
print(sys.getsizeof(is_mersenne_prime))

