# Select the smallest element from the unsorted part and put it at the beginning.

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