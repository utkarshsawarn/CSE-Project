import sys
import time
start_time=time.time()

def mod_exp(base, exponent, modulus):
    
    if modulus <= 0:
        raise ValueError("Modulus must be a positive integer.")
    if exponent < 0:
        raise ValueError("Exponent must be a non-negative integer.")
    result = 1
    base = base % modulus
    while exponent > 0:
        
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent = exponent // 2
        base = (base * base) % modulus

    return result


base_val = 2
exponent_val = 10
modulus_val = 3
result = mod_exp(base_val, exponent_val, modulus_val)
print(f"({base_val}**{exponent_val}) % {modulus_val} = {result}")

base_large = 5
exponent_large = 100
modulus_large = 13
result_large = mod_exp(base_large, exponent_large, modulus_large)
print(f"({base_large}**{exponent_large}) % {modulus_large} = {result_large}")

print("---%s seconds ---"%(time.time() - start_time))
print(sys.getsizeof(mod_exp))


