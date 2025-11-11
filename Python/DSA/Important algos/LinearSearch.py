def linear_search(list, target):
    """
    ---- Doc string ---- 
    Return the index position of the target if found, else returns None
    """

    for i in range(0, len(list)):
        if list[i] == target:
           return i
    return None

def ls(index):
    if index is not None:
        print("Target found at index:",index)
    else:
        print("Target not found in list")

n=[1,2,3,4,6,7,8,34,22]

res=linear_search(n,3)
ls(res)

res=linear_search(n,44)
ls(res)
