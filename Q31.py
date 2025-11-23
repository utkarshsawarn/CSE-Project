import time
import tracemalloc

start_time =  time.time()
tracemalloc.start()

def lucas_sequence(n):
    if n<=0:
        raise ValueError
    if n==1:
        return[2]
    sequence = [2,1]
    for i in range(2,n):
        sequence.append(sequence[-1]+sequence[-2])
    return sequence

end_time = time.time()
curr , max = tracemalloc.get_traced_memory()

print(lucas_sequence(7))
print(f"Execution Time: {end_time - start_time} seconds")
print(f"Current Memory Usage for the above code is : {curr} bytes")
print(f"Max memory usage for the above code is {max} bytes")