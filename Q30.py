#25)
import math

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def is_perfect_square(k):
    if k < 0:
        return False
    if k == 0:
        return True
    # Using math.isqrt is more robust and efficient for integer square roots in Python 3.8+
    # For compatibility, using **0.5 with int() is also common.
    s = int(k**0.5) 
    return s * s == k

def is_fibonacci(n):
    if n <= 0:
        return False
    # A positive integer n is a Fibonacci number if and only if
    # 5n^2 + 4 or 5n^2 - 4 is a perfect square.
    return is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4)

# --- Function Call Examples ---

# 1. Check a known Fibonacci number (e.g., 21)
f1 = 21
check1 = is_fibonacci(f1)
print(f"Is {f1} a Fibonacci number? {check1}") # Expected: True (5 * 21^2 + 4 = 2209, sqrt(2209) = 47)

# 2. Check a non-Fibonacci number (e.g., 14)
f2 = 14
check2 = is_fibonacci(f2)
print(f"Is {f2} a Fibonacci number? {check2}") # Expected: False

# 3. Check the smallest Fibonacci number (e.g., 1)
f3 = 1
check3 = is_fibonacci(f3)
print(f"Is {f3} a Fibonacci number? {check3}") # Expected: True
