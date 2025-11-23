import sys
import time
start_time=time.time()

def multiplicative_persistence(n):
        if n < 10:
            return 0  

        persistence_count = 0
        current_number = n

        while current_number >= 10:
            product = 1
            for digit_char in str(current_number):
                product *= int(digit_char)
        
            current_number = product
            persistence_count += 1
        
        return persistence_count
p=multiplicative_persistence(456789)
print(p)

print("---%s seconds ---"%(time.time() - start_time))
print(sys.getsizeof(multiplicative_persistence))
