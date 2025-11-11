def binary_search(list, target):
    left = 0
    right = len(list) - 1


    while left <= right:
        
        mid = (left + right)//2 # rounds

        if list[mid] == target:
            return mid
        elif list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return None

def bs(index):
    if index is not None:
        print("Target found at index:",index)
    else:
        print("Target not found in list")

n=[1,2,3,4,6,7,8,34,22]

res=binary_search(n,34)
bs(res)

res=binary_search(n,44)
bs(res)
