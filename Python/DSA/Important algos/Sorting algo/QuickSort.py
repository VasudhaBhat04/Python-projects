# Choose a pivot → partition the array into smaller & greater elements → recursively sort each part.

def partition(arr, low, high):
    pivot = arr[high]  # choose last element as pivot
    i = low - 1        # pointer for smaller element

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # swap

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

"""
Time Complexity:

Best/Average: O(n log n)

Worst: O(n²) (bad pivot selection)

Space: O(log n)


"""

"""
def quick_sort(arr):
    if len(arr) <= 1:
        return arr   # base case — already sorted

    pivot = arr[len(arr) // 2]  # choose middle element as pivot
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)



"""
    