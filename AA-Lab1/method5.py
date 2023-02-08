#MATRIX EXPONENTIATION METHOD 

# Import time module
import time
 
# record start time
start = time.time()


# code 
def matrix_mult(A, B):
    C = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                C[i][j] += A[i][k] * B[k][j]
    return C

def matrix_pow(A, n):
    if n == 0:
        return [[1, 0], [0, 1]]
    elif n % 2 == 0:
        B = matrix_pow(A, n//2)
        return matrix_mult(B, B)
    else:
        B = matrix_pow(A, n-1)
        return matrix_mult(A, B)

def fibonacci(n):
    if n <= 0:
        return 0
    else:
        F = matrix_pow([[1, 1], [1, 0]], n-1)
        return F[0][0]

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
