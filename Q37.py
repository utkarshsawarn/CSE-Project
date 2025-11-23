#32)
import random
import math

def gcd(a, b):
    return math.gcd(a, b)

def pollard_rho(n):
    if n <= 1:
        return None
    if n % 2 == 0:
        return 2
    
    # Check if n is prime before starting the algorithm (optional but good practice)
    # A simple primality test could be added here, but we proceed with the core algorithm.

    x = random.randint(2, n - 1)
    y = x
    c = random.randint(1, n - 1)
    d = 1
    
    # Define the pseudo-random function f(x) = (x^2 + c) mod n
    def f(x):
        return (x * x + c) % n

    # The loop implements Floyd's cycle-finding algorithm (tortoise and hare)
    while d == 1:
        x = f(x)
        y = f(f(y))
        
        # d = gcd(|x - y|, n)
        d = gcd(abs(x - y), n)

        if d == n:
            # Cycle detected without finding a factor, restart with new initial values
            # This happens if the cycle forms entirely within the group of residues modulo n, 
            # and no collision has occurred modulo a factor p.
            x = random.randint(2, n - 1)
            y = x
            c = random.randint(1, n - 1)
            d = 1
        elif d != 1:
            # We found a non-trivial factor
            return d

    return d # Should be unreachable if the logic is correct, but kept for completeness

# --- Function Call Examples ---

# 1. Factor a small composite number (e.g., 91 = 7 * 13)
n1 = 91
factor1 = pollard_rho(n1)
print(f"A factor of {n1} is: {factor1}")

# 2. Factor another composite number (e.g., 87 = 3 * 29)
n2 = 87
factor2 = pollard_rho(n2)
print(f"A factor of {n2} is: {factor2}")

# 3. Factor a number with a small prime factor (e.g., 143 = 11 * 13)
n3 = 143
factor3 = pollard_rho(n3)
print(f"A factor of {n3} is: {factor3}")
