import time
import sys

var=1

start_time=time.time()

def is_palindrome(n):
    s=str(n)
    return s==s[::-1]

n=int(input("Enter the number:"))        
print(is_palindrome(n))

end_time=time.time()

execution_time=end_time-start_time

print("Execution time:",execution_time)
print(sys.getsizeof(var))