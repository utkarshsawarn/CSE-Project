import math
import time
import tracemalloc

start_time =  time.time()
tracemalloc.start()

def gcd(a,b):
    while b:
        a, b = b, a%b
    return a

def is_carmichael(n):
    if n<2 :
        return False
    if all(n % i != 0 for i in range(2, int(math.sqrt(n)) + 1)):
        return False
    for a in range(2, n):
        if gcd(a, n) ==1:
           if pow(a, n-1, n) != 1:
              return False
    return True

end_time = time.time()
curr , max = tracemalloc.get_traced_memory()

print(gcd(7,5) ,is_carmichael(81))
print(f"Execution Time: {end_time - start_time} seconds")
print(f"Current Memory Usage for the above code is : {curr} bytes")
print(f"Max memory usage for the above code is {max} bytes")