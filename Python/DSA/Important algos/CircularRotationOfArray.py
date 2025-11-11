# Circular rotation means you shift the array elements left or right, and the elements that go out on one side come back around to the other side.
#Array rotation or array shifting

#Right rotation
def right_rotate(arr, k):
    n = len(arr)
    k = k % n  # handle cases where k > n
    return arr[-k:] + arr[:-k] #k -> no. of rotations

arr = [1, 2, 3, 4, 5]
print(right_rotate(arr, 2))

#Left rotation
def left_rotate(arr, k):
    n = len(arr)
    k = k % n
    return arr[k:] + arr[:k]

arr = [1, 2, 3, 4, 5]
print(left_rotate(arr, 2))

#Using loops 1 rotation
def right_rotate_once(arr):
    last = arr[-1]
    for i in range(len(arr)-1, 0, -1):
        arr[i] = arr[i-1]
    arr[0] = last
    return arr

"""
Slicing in Python:Slicing is a way to extract a portion of a sequence (like a list, string, or tuple) by specifying start, stop, and step indices.

sequence[start : stop : step]

start → index where the slice begins (inclusive)

stop → index where the slice ends (exclusive)

step → how many elements to skip at a time (optional)

arr = [10, 20, 30, 40, 50, 60]

| Expression  | Output                     | Explanation                    |
| ----------- | -------------------------- | ------------------------------ |
| `arr[1:4]`  | `[20, 30, 40]`             | elements from index 1 to 3     |
| `arr[:3]`   | `[10, 20, 30]`             | from start to index 2          |
| `arr[2:]`   | `[30, 40, 50, 60]`         | from index 2 to end            |
| `arr[-2:]`  | `[50, 60]`                 | last 2 elements                |
| `arr[:-1]`  | `[10, 20, 30, 40, 50]`     | everything except last element |
| `arr[::2]`  | `[10, 30, 50]`             | every 2nd element              |
| `arr[::-1]` | `[60, 50, 40, 30, 20, 10]` | reversed list                  |











"""