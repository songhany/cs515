def last_index(arr, target):
    """
    :param: arr - input array
    :param: target - integer element
    return: int - last index of target in arr
    TODO: complete this method to find the last index of target in arr
    """
    return recursion(arr, target, len(arr) - 1)

def recursion(arr, target, idx):
    if idx < 0:
        return -1
    
    if arr[idx] == target:
        return idx
    
    return recursion(arr, target, idx - 1)