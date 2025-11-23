#21)
def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    
    g, x1, y1 = extended_gcd(b % a, a)
    
    x = y1 - (b // a) * x1
    y = x1
    
    return g, x, y

def mod_inverse(a, m):
    g, x, y = extended_gcd(a, m)
    
    if g != 1:
        return None
    else:
        return (x % m + m) % m

# --- Function Call Examples ---

a1 = 3
m1 = 11
inverse1 = mod_inverse(a1, m1)
print(f"The modular inverse of {a1} mod {m1} is: {inverse1}")

a2 = 17
m2 = 20
inverse2 = mod_inverse(a2, m2)
print(f"The modular inverse of {a2} mod {m2} is: {inverse2}")

a3 = 6
m3 = 12
inverse3 = mod_inverse(a3, m3)
print(f"The modular inverse of {a3} mod {m3} is: {inverse3}")
