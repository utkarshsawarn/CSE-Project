import sys
import time

def is_automorphic(n):
   
    if n < 0:
        n = -n # Automorphic property applies to the absolute value 
    square = n * n
    
    # Convert both the number and its square to strings for easy comparison of endings
    str_n = str(n)
    str_square = str(square)

    return str_square.endswith(str_n)

print(f"Is 5 automorphic? {is_automorphic(5)}")
print(f"Is 6 automorphic? {is_automorphic(6)}")
print(f"Is 25 automorphic? {is_automorphic(25)}")
print(f"Is 76 automorphic? {is_automorphic(76)}")
print(f"Is 7 automorphic? {is_automorphic(7)}")

print("---%s seconds ---"%(time.time() - start_time))
print(sys.getsizeof(is_automorphic))
