def count_distinct_prime_factors(n):
   
    if n <= 1:
        return 0  
    distinct_prime_factors = set()
    d = 2

    while n % d == 0:
        distinct_prime_factors.add(d)
        n //= d

    # odd factors
    d = 3
    while d * d <= n:
        while n % d == 0:
            distinct_prime_factors.add(d)
            n //= d
        d += 2

    # If n is still greater than 1, it must be a prime factor itself
    if n > 1:
        distinct_prime_factors.add(n)

    return len(distinct_prime_factors)
print(count_distinct_prime_factors(65445))
print(count_distinct_prime_factors(2434))
