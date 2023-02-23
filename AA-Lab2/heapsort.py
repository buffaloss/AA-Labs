import time
import random

start = time.time()

#heap sort algorithm for sorting the eleemnts of the array in ascending order
def heap_sort(arr):
    n = len(arr)
    
    # create a max-heap from the array
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    # take the elements from the max-heap one after another
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # swap the root and last element
        heapify(arr, i, 0)  # heapify the reduced heap
    
    return arr

#fucntion for verifying if the subtree is a maxheap ( at index i)
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    # Find the largest element among i, left child, and right child
    if left < n and arr[left] > arr[largest]:
        largest = left
        
    if right < n and arr[right] > arr[largest]:
        largest = right
        
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap those  elements
        heapify(arr, n, largest)  # recursively heapify the affected subtree, calling the same function from inside

def array_generator(n):
    #generate an array of size n
    #choose which ranges you want for the inetegers themselves - i used the range for each value  0 - 100.000
    return [random.randint(0, 100000) for _ in range(n)]

 #Generate a random array of size (...)
random_array = array_generator(800000)

sorted_array = heap_sort(random_array)

end = time.time()
print("Exec time: ",(end-start) * 10**3, "ms")
