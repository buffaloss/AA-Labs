#BINET'S FORMULA METHOD / CLOSED-FORM EXPRESSION

# Import time module
import time
import math
 
# record start time
start = time.time()


# code 
def fibonacci(n):
    phi = (1 + math.sqrt(5)) / 2
    psi = (1 - math.sqrt(5)) / 2
    return int((phi**n - psi**n) / math.sqrt(5))

if __name__ == '__main__':
    n = 1585
    result = fibonacci(n)
    print(result)


# record end time
end = time.time()
# print the difference between start
# and end time in milli. secs
print("Execution time:",
      (end-start) * 10**3, "ms")
