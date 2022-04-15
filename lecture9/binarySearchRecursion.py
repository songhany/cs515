# not right
def binarySearchRecursion(lst, left, right, target):

    if left <= right:
        mid = left + (right - left) // 2

        if lst[mid] == target:
            return mid
        elif lst[mid] > target:
            return binarySearchRecursion(lst, left, mid-1, target)
        else:
            return binarySearchRecursion(lst, mid+1, right, target)
    else:
        return -1

arr = [1, 2, 3, 4, 5, 6, 7]
print(binarySearchRecursion(arr, 0, len(arr), 5))
print(binarySearchRecursion(arr, 0, len(arr), 1))

