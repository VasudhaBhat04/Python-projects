# Convert array into a heap, repeatedly extract the max element, and rebuild the heap.
def heapify(arr, n, i):
    largest = i     # Initialize largest as root
    l, r = 2*i + 1, 2*i + 2    # left index = 2*i + 1 , right index = 2*i + 2

    # If left child is larger than root
    if l < n and arr[l] > arr[largest]:
        largest = l

    # If right child is larger than largest so far
    if r < n and arr[r] > arr[largest]:
        largest = r
 
    # If largest is not root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr

if __name__ == "__main__":
    arr = [9, 4, 3, 8, 10, 2, 5]

    heap_sort(arr)

    for i in range(len(arr)):
        print(arr[i], end=" ")
