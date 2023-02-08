#THE ITERATIVE METHOD (USING LOOP)

# Import time module
import time
 
# record start time
start = time.time()


# code 
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for i in range(2, n+1):
            c = a + b
            a, b = b, c
        return b

if __name__ == '__main__':
    n = 12589
    result = fibonacci(n)
    print(result)


# record end time
end = time.time()
# print the difference between start
# and end time in milli. secs
print("Execution time:",
      (end-start) * 10**3, "ms")
