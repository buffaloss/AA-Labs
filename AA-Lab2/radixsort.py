import time
import random

start = time.time()

#fucntion for radix sorting algorithm in ascending order
def radix_sort(arr):
    max_val = max(arr) #set max_value in the shoel array 
    exp = 1
    while max_val // exp > 0: #sorts through teh numbers by each digit 
        counting_sort(arr, exp)
        exp *= 10 

def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n #array for teh already sorted eleemnets
    count = [0] * 10 #nr f occurences of each digit
    for i in range(n): #loop and increse the value for digit each time
        index = arr[i] // exp
        count[index % 10] += 1
    # Perform a prefix sum on the count array to get the starting indices of each digit in the sorted output
    for i in range(1, 10):
        count[i] += count[i-1]
      # Loop over the array in reverse order and place each element in the correct position in the output array
    for i in range(n-1, -1, -1):
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
    # Copy the sorted output array back into the original array
    for i in range(n):
        arr[i] = output[i]


def array_generator(n):
    #generate an array of size n
    #choose which ranges you want for the inetegers themselves - i used the range for each value  0 - 100.000
    return [random.randint(0, 100000) for _ in range(n)]

 #Generate a random array of size (...)
random_array = array_generator(800000)

sorted_array = radix_sort(random_array)

end = time.time()
print("Exec time: ",(end-start) * 10**3, "ms")
