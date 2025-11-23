#23) 
def power(a, b, m):
    res = 1
    a = a % m
    while b > 0:
        if b % 2 == 1:
            res = (res * a) % m
        b = b // 2
        a = (a * a) % m
    return res

# --- Function Call Example (Modular Exponentiation) ---

# Calculate 3^5 mod 7
a = 3
b = 5
m = 7

result = power(a, b, m)

print(f"The result of {a}^{b} mod {m} is: {result}")

# Verification:
# 3^1 mod 7 = 3
# 3^2 mod 7 = 9 mod 7 = 2
# 3^3 mod 7 = 6 mod 7 = 6
# 3^4 mod 7 = 18 mod 7 = 4
# 3^5 mod 7 = 12 mod 7 = 5 (Correct)


# Another Example: Calculate 2^10 mod 13
a2 = 2
b2 = 10
m2 = 13

result2 = power(a2, b2, m2)

print(f"The result of {a2}^{b2} mod {m2} is: {result2}")

# Verification:
# 2^10 = 1024
# 1024 mod 13 = 1024 - (78 * 13) = 1024 - 1014 = 10 (Correct)
