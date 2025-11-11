# Repeatedly swap adjacent elements if they’re in the wrong order

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr

def sort(res):
    print(res)

a = [4,3,7,91,23,56,990,12,1004,121]

r = bubble_sort(a)
sort(r)