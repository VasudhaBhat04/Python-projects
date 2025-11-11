# Convert array into a heap, repeatedly extract the max element, and rebuild the heap.
"""
A heap is a special kind of binary tree that satisfies the heap property:
Max Heap:
The parent node is always greater than or equal to its children.
→ So the largest element is always at the root (index 0).Ascending order sort
Min Heap:
The parent node is always smaller than or equal to its children.
→ So the smallest element is always at the root.Descending order sort.

Heap sort typically uses a Max Heap (for ascending order sort):

Build a Max Heap from the array.
→ So the largest element is at index 0.

Swap the largest element (root) with the last element.

Reduce heap size (ignore the sorted last element).

Heapify the root again to maintain max heap.

Repeat until the entire array is sorted.

"""

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

"""
Time Complexity:

Best/Worst/Average: O(n log n)

Space: O(1)

"""