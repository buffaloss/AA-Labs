#DYNAMIC PROGRAMMING METHOD (MEMOIZATION)

# Import time module
import time
import sys
sys.setrecursionlimit(13000)
 
# record start time
start = time.time()


# code 
def fibonacci(n, memo={}):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n in memo:
        return memo[n]
    else:
        memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
        return memo[n]

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

