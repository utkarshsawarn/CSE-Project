def is_prime(n):
   
    if n < 2:
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

def twin_primes(limit):
   
    twin_prime_pairs = []
    for num in range(3, limit - 1):  # Start from 3 as 2 is not part of a twin prime pair (2,4)
        if is_prime(num) and is_prime(num + 2):
            twin_prime_pairs.append((num, num + 2))
    return twin_prime_pairs
print(is_prime(65779))
print(twin_primes(8))
