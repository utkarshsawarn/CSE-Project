def is_harshad(n):
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer.")

    sum_of_digits = 0
    temp_n = n
    while temp_n > 0:
        sum_of_digits += temp_n % 10
        temp_n //= 10

    return n % sum_of_digits == 0

print(is_harshad(4563897))
print(is_harshad(7698707))
print(is_harshad(5658))
