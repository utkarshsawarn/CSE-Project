  #22)
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

def crt(remainders, moduli):
    if not remainders or not moduli or len(remainders) != len(moduli):
        return None
    
    x = remainders[0]
    M = moduli[0]
    
    for i in range(1, len(moduli)):
        r_i = remainders[i]
        m_i = moduli[i]
        
        b = r_i - x
        
        M_inv = mod_inverse(M, m_i)
        
        if M_inv is None:
            return None
            
        k = (b * M_inv) % m_i
        
        x = x + k * M
        
        M = M * m_i
        
    return x % M

# --- Function Call Example (Chinese Remainder Theorem) ---

remainders = [2, 3, 2]
moduli = [3, 5, 7]

solution = crt(remainders, moduli)

print(f"The system of congruences:")
print(f"x ≡ {remainders[0]} (mod {moduli[0]})")
print(f"x ≡ {remainders[1]} (mod {moduli[1]})")
print(f"x ≡ {remainders[2]} (mod {moduli[2]})")

if solution is not None:
    print(f"\nThe smallest non-negative solution for x is: {solution}")
else:
    print("\nNo unique solution exists (mod M) because the moduli are not pairwise coprime.")
