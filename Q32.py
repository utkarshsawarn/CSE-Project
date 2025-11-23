import math
import time
import tracemalloc

start_time =  time.time()
tracemalloc.start()

def is_perfect_power(n):
    if n < 2:
        return False
    for b in range(2, int(math.log2(n)) + 1):
        a = round(n**(1.0 / b))
        for base in (a, a-1, a+1):
            if base> 1 and base ** b == n:
                return True
    return False

end_time = time.time()
curr , max = tracemalloc.get_traced_memory()

print(is_perfect_power(16))
print(f"Execution Time: {end_time - start_time} seconds")
print(f"Current Memory Usage for the above code is : {curr} bytes")
print(f"Max memory usage for the above code is {max} bytes")