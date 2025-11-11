def recursive_binary_search(list, target):
    if len(list) == 0:
        return False
    else :
        mid = (len(list))//2

    if list[mid] == target:
        return True
    else:
        if list[mid]<target:
          return recursive_binary_search(list[mid+1:],target)
        else:
           return recursive_binary_search(list[:mid],target)

def bs(result):
        print("Target found ?:",result)
    

n=[1,2,3,4,6,7,8,34,22]

res=recursive_binary_search(n,34)
bs(res)

res=recursive_binary_search(n,44)
bs(res)