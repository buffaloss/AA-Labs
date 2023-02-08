#RECURSIVE METHOD

# Import time module
import time
 
# record start time
start = time.time()
 

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

if __name__ == '__main__':
    n = 40 # here we put which element we want
    result = fibonacci(n)
    print( result)

# record end time
end = time.time()
# print the difference between start
# and end time in milli. secs
print("Execution time:",
      (end-start) * 10**3, "ms")
