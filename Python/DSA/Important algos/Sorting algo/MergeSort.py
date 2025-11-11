# Divide the array into halves, recursively sort each half, then merge them.

def merge_sort(arr):
    if len(arr)>1:
        mid = len(arr)//2
        left = arr[:mid]  #divide
        right = arr[mid:]

        merge_sort(left) #sort left half
        merge_sort(right) # sort right half

        i = j = k = 0  # i->left, j->right, k->merged
       
        # merge the two halves as well as go on sorting 
        while i <len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else :
                arr[k] = right[j]
                j += 1
            k += 1
        

        # add any remaining elements
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    return arr
def sort(res):
    print(res)

a = [4,3,7,91,23,56,990,12,1004,121]

r = merge_sort(a)
sort(r)

"""
Time Complexity:

Best/Worst/Average: O(n log n)

Space: O(n)

"""
"""
def merge(arr, beg, mid, end):
    n1 = mid - beg + 1
    n2 = end - mid

    # create temp arrays
    left = arr[beg:mid + 1]
    right = arr[mid + 1:end + 1]

    i = j = 0
    k = beg

    # merge the temp arrays back into arr[beg:end+1]
    while i < n1 and j < n2:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    # copy remaining elements
    while i < n1:
        arr[k] = left[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = right[j]
        j += 1
        k += 1


def merge_sort(arr, beg, end):
    if beg < end:
        mid = (beg + end) // 2
        merge_sort(arr, beg, mid)
        merge_sort(arr, mid + 1, end)
        merge(arr, beg, mid, end)



arr = [6, 3, 9, 5, 2, 8]
merge_sort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)



"""