#33)
import math

def zeta_approx(s, terms):
    if s == 1:
        # Harmonic series diverges, but we'll return the sum up to 'terms'
        pass
    
    zeta_sum = 0
    for n in range(1, terms + 1):
        try:
            term = 1.0 / math.pow(n, s)
            zeta_sum += term
        except OverflowError:
            return float('inf') 
        except ZeroDivisionError:
            pass

    return zeta_sum

# --- Function Call Examples ---

# Known value: zeta(2) = pi^2 / 6 ≈ 1.644934
s1 = 2
terms1 = 1000
approximation1 = zeta_approx(s1, terms1)
exact_value1 = (math.pi**2) / 6
print(f"Approximation of Zeta({s1}) using {terms1} terms: {approximation1}")
print(f"Known exact value of Zeta({s1}): {exact_value1}")

print("-" * 30)

# Known value: zeta(4) = pi^4 / 90 ≈ 1.082323
s2 = 4
terms2 = 100
approximation2 = zeta_approx(s2, terms2)
exact_value2 = (math.pi**4) / 90
print(f"Approximation of Zeta({s2}) using {terms2} terms: {approximation2}")
print(f"Known exact value of Zeta({s2}): {exact_value2}")

print("-" * 30)

# Case s=1 (Harmonic Series) - Diverges
s3 = 1
terms3 = 1000
approximation3 = zeta_approx(s3, terms3)
print(f"Approximation of Zeta({s3}) (Harmonic Series) using {terms3} terms: {approximation3}")
