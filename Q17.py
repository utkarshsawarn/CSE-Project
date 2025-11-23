import math

def is_prime_power(n):
    """
    Checks if a number n is a prime power (p^k where p is prime and k >= 1).
    """
    if n <= 1:
        return False

    # Find the smallest prime factor, p
    p = -1
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            p = i
            break
    
    # If no factor was found within the loop, n itself is prime
    if p == -1:
        p = n
    
    # Check if n can be fully divided by only this single prime factor p
    temp_n = n
    while temp_n % p == 0:
        temp_n //= p
        
    # If temp_n becomes 1, then n was a power of p
    return temp_n == 1

# Examples:
print(f"8 is a prime power: {is_prime_power(8)}")       # 8 = 2^3 -> True
print(f"12 is a prime power: {is_prime_power(12)}")     # 12 = 2^2 * 3 -> False
print(f"1 is a prime power: {is_prime_power(1)}")       # False by definition
