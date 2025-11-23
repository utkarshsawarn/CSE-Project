import time
import sys

def digital_root(n):
    num = abs(n)
    
    while num >= 10:
        digit_sum = 0
        while num > 0:
            digit_sum += num % 10  
            num //= 10           
        num = digit_sum
    
    return num

def main():
    try:
        n = int(input("Enter a number: "))
        
        # Start timing
        start_time = time.time()
        
        # Calculate digital root
        result = digital_root(n)
        
        # End timing
        end_time = time.time()
        
        # Display results
        print(f"Digital root of {n} is: {result}")
        print("-" * 40)
        print(f"Execution Time: {end_time - start_time:.6f} seconds")
        print(f"Memory utilization: {sys.getsizeof(n)} bytes")
            
    except ValueError:
        print("Error: Please enter a valid integer.")

if __name__ == "__main__":
    main()