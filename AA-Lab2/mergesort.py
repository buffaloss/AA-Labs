import time
import random

start = time.time()

#function for sorting array using Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr #if its length is one or less, it doesn't even need to be sorted
    
    middle = len(arr) // 2 #split the array in 2
    left_arr = arr[:middle]
    right_arr = arr[middle:]
    
    left_arr = merge_sort(left_arr)
    right_arr = merge_sort(right_arr)
    
    return merge(left_arr, right_arr)

#fucntion for combining 2 sorted arryas into one whole array
#is called in the merge_sort function above ^
def merge(l, r):
    result = []
    i, j = 0, 0
    
    while i < len(l) and j < len(r):
        if l[i] <= r[j]:
            result.append(l[i])
            i += 1
        else:
            result.append(r[j])
            j += 1
            
    result += l[i:]
    result += r[j:]
    
    return result

def array_generator(n):
    #generate an array of size n
    #choose which ranges you want for the inetegers themselves - i used the range for each value  0 - 100.000
    return [random.randint(0, 100000) for _ in range(n)]

 #Generate a random array of size (...)
random_array = array_generator(800000)

sorted_array = merge_sort(random_array)

end = time.time()
print("Exec time: ",(end-start) * 10**3, "ms")
