import time
import random

start = time.time()

#function for sorting using Quick Sort algorithm
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]  #set the first element as the pivot 
    left = []
    right = []
    
    for elem in arr[1:]:
        if elem <= pivot:
            left.append(elem)
        else:
            right.append(elem)
    
    # recursively sort the left and right subarrays
    left = quick_sort(left)
    right = quick_sort(right)
    
    return left + [pivot] + right


def array_generator(n):
    #generate an array of size n
    #choose which ranges you want for the inetegers themselves - i used the range for each value  0 - 100.000
    return [random.randint(0, 100000) for _ in range(n)]

 #Generate a random array of size (...)
random_array = array_generator(800000)

sorted_array = quick_sort(random_array)

end = time.time()
print("Exec time: ",(end-start) * 10**3, "ms")
