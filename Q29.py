#24)
import math

def gcd(a, b):
    # This is a standard implementation using the math library or Euclidean algorithm
    return math.gcd(a, b)

def order_mod(a, n):
    if gcd(a, n) != 1:
        return None 
    
    k = 1
    current_power = a % n
    
    while current_power != 1:
        current_power = (current_power * a) % n
        k += 1
        
        if k > n: 
            return None 

    return k

# --- Function Call Example ---

# 1. Find the order of 3 modulo 7: ord_7(3)
# Sequence: 3^1=3, 3^2=2, 3^3=6, 3^4=4, 3^5=5, 3^6=1 (mod 7)
a1 = 3
n1 = 7
order1 = order_mod(a1, n1)
print(f"The order of {a1} mod {n1} is: {order1}") # Expected: 6

# 2. Find the order of 2 modulo 5: ord_5(2)
# Sequence: 2^1=2, 2^2=4, 2^3=3, 2^4=1 (mod 5)
a2 = 2
n2 = 5
order2 = order_mod(a2, n2)
print(f"The order of {a2} mod {n2} is: {order2}") # Expected: 4

# 3. Example where gcd(a, n) != 1: Find the order of 4 modulo 6 (gcd(4, 6) = 2)
a3 = 4
n3 = 6
order3 = order_mod(a3, n3)
print(f"The order of {a3} mod {n3} is: {order3}") # Expected: None
