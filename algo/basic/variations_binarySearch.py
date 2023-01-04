def recursive_binary_search(target, arr, left=0):
    if len(arr) == 0:
        return None

    center = (len(arr)-1) // 2
    if arr[center] == target:
        return center + left
    elif arr[center] < target:
        return recursive_binary_search(target, arr[center+1:], left + center+1)
    else:
        return recursive_binary_search(target, arr[:center], left)


def find_first(target, arr):
    index = recursive_binary_search(target, arr)
    if not index:
        return None
    while arr[index] == target:
        if index == 0:
            return 0
        if arr[index-1] == target:
            index -= 1
        else:
            return index

            
multiple = [1, 3, 5, 7, 7, 7, 8, 11, 12, 13, 14, 15]
print(find_first(7, multiple)) # Should return 3
print(find_first(9, multiple)) # Should return None


def find_first_mySol(target, source):
    if len(source) == 0:
        return None
    
    left = 0;
    right = len(source) - 1
    while left < right - 1:
        mid = left + (right - left) // 2
        if source[mid] >= target:
            right = mid
        else:
            left = mid + 1

    if source[left] == target:
        return left
    elif source[right] == target:
        return right
    
    return None