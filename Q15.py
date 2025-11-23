def prime_factors(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2

    # We only need to check up to the square root of n
    i = 3
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n //= i
        i += 2  # Increment by 2 to check only odd numbers

    # If n is still greater than 2, it means n itself is a prime factor
    if n > 2:
        factors.append(n)

    return factors

print(prime_factors(675412))
print(prime_factors(23247))
print(prime_factors(3764))
