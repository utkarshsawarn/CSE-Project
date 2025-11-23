import time
import tracemalloc

start_time =  time.time()
tracemalloc.start()

def collatz_lenght(n):
    if n<= 0:
        raise ValueError("Input must be a positive integer.")
    
    steps = 0
    while n !=1:
        if n % 2==0:
            n //= 2 
        else:
            n = 3*n+1
        steps += 1
    return steps
end_time = time.time()
curr , max = tracemalloc.get_traced_memory()
    
print(collatz_lenght(6))
print(collatz_lenght(19))
print(f"Execution Time: {end_time - start_time} seconds")
print(f"Current Memory Usage for the above code is : {curr} bytes")
print(f"Max memory usage for the above code is {max} bytes")