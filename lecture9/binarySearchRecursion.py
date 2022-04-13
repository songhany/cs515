# not right
def binarySearchRecursion(lst, target):
    if (lst == [] or len(lst) == 0):
        return 

    left = 0;
    right = len(lst) - 1
    
    mid = left + (right - left) // 2
    if target == lst[mid]:
        return mid
    elif target > lst[mid]:
        return binarySearchRecursion(lst[mid: right+1], target)
    else:
        return binarySearchRecursion(lst[left: mid], target)

# print(binarySearchRecursion([1, 2, 3, 4, 5, 6, 7], 5))


