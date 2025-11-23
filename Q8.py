import time
import sys

def is_abundant(n):
    if n < 1:
        return False
    if n == 1:
        return False  # 1 is not abundant
    
    sum_divisors = 1  # 1 is always a proper divisor
    i = 2
    while i * i <= n:
        if n % i == 0:
            if i != n // i:
                sum_divisors += i + n // i
            else:
                sum_divisors += i
        i += 1
    
    return sum_divisors > n

def main():
    n = int(input("Enter a number: "))
    
    start_time = time.time()
    result = is_abundant(n)
    end_time = time.time()
    
    if result:
        print(n, "is an abundant number.")
    else:
        print(n, "is not an abundant number.")
    
    print("Execution time:", end_time - start_time, "seconds")
    print("Memory used:", sys.getsizeof(n) + sys.getsizeof(result) + 
          sys.getsizeof(start_time) + sys.getsizeof(end_time), "bytes")

if __name__ == "__main__":
    main()