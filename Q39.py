#34)
def partition_function(n):
    if n < 0:
        return 0
    if n == 0:
        return 1

    p = [0] * (n + 1)
    p[0] = 1

    for i in range(1, n + 1):
        j = 1
        while True:
            # Generalized pentagonal number k(3k-1)/2
            g1 = j * (3 * j - 1) // 2
            
            # The sign pattern is based on k: k=1, 2 have sign +, k=3, 4 have sign -, etc.
            # Sign is determined by j: 1, 2 (j=1), 3, 4 (j=2), ...
            sign = (-1)**(j - 1)
            
            if i - g1 >= 0:
                p[i] += sign * p[i - g1]
            else:
                break
                
            # Second generalized pentagonal number k(3k+1)/2
            g2 = j * (3 * j + 1) // 2
            
            if i - g2 >= 0:
                p[i] += sign * p[i - g2]
            else:
                break

            j += 1
            
    return p[n]

# --- Function Call Examples ---

# 1. Calculate p(5): 5, 4+1, 3+2, 3+1+1, 2+2+1, 2+1+1+1, 1+1+1+1+1. Total 7.
n1 = 5
result1 = partition_function(n1)
print(f"The number of partitions for n={n1} is: {result1}")

# 2. Calculate p(10): Total 42.
n2 = 10
result2 = partition_function(n2)
print(f"The number of partitions for n={n2} is: {result2}")

# 3. Calculate p(20): Total 627.
n3 = 20
result3 = partition_function(n3)
print(f"The number of partitions for n={n3} is: {result3}")
