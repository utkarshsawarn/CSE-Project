import time
import sys

def factorial(n):
    """
    Calculate factorial of a non-negative integer using iterative approach.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def main():
    try:
        n = int(input("Enter a non-negative integer: "))
        
        start_time = time.time()
        result = factorial(n)
        end_time = time.time()
        
        print(f"{n}! = {result}")
        print(f"Execution Time: {end_time - start_time:.6f} seconds")
        print(f"Memory utilization: {sys.getsizeof(result)} bytes")
        
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()