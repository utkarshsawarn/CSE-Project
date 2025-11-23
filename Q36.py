#31
import random

def power(a, b, m):
    res = 1
    a = a % m
    while b > 0:
        if b % 2 == 1:
            res = (res * a) % m
        b = b // 2
        a = (a * a) % m
    return res

def is_prime_miller_rabin(n, k=5):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1

    for _ in range(k):
        # random.randint(2, n - 2) might fail if n <= 3, but is handled by base cases
        a = random.randint(2, n - 2)
        x = power(a, d, n)

        if x == 1 or x == n - 1:
            continue
        
        composite = True
        for _ in range(s - 1):
            x = (x * x) % n
            if x == n - 1:
                composite = False
                break
        
        if composite:
            return False

    return True

# --- Function Call Examples ---

# 1. Test a known prime number (53)
n1 = 53
result1 = is_prime_miller_rabin(n1)
print(f"Is {n1} prime? (Miller-Rabin): {result1}")

# 2. Test a known composite number (51 = 3 * 17)
n2 = 51
result2 = is_prime_miller_rabin(n2)
print(f"Is {n2} prime? (Miller-Rabin): {result2}")

# 3. Test a large prime number (997)
n3 = 997
result3 = is_prime_miller_rabin(n3)
print(f"Is {n3} prime? (Miller-Rabin): {result3}")
