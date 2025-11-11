# Select the smallest element from the unsorted part and put it at the beginning.
# It sorts an array by repeatedly selecting the smallest (or largest) element from the unsorted portion and swapping it with the first unsorted element. This process continues until the entire array is sorted.
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min = i
        for j in range(i+1,n):
            if arr[j]<arr[min]:
                min = j
        arr[i],arr[min]=arr[min],arr[i]
    return arr

def sort(res):
    print(res)

a = [4,3,7,91,23,56,990,12,1004,121]

r = selection_sort(a)
sort(r)

"""
Time Complexity:

Best/Worst/Average: O(n²)

Space: O(1)

"""