import time
import tracemalloc
start_time =  time.time()
tracemalloc.start()
def polygonal_number(s,n):
    p = ((s-2)*(n**2) -(s-4)*n)//2
    return p

end_time = time.time()
curr , max = tracemalloc.get_traced_memory()

print(polygonal_number(3,5))

print(f"Execution Time: {end_time - start_time} seconds")
print(f"Current Memory Usage for the above code is : {curr} bytes")
print(f"Max memory usage for the above code is {max} bytes")