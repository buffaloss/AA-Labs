#GENERATORS METHOD

# Import time module
import time
 
# record start time
start = time.time()


# code 
def fibonacci():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b

def nth_fibonacci(n):
    for i, f in enumerate(fibonacci()):
        if i == n-1:
            return f


if __name__ == '__main__':
    n = 12589
    result = nth_fibonacci(n)
    print(result)


# record end time
end = time.time()
# print the difference between start
# and end time in milli. secs
print("Execution time:",
      (end-start) * 10**3, "ms")
