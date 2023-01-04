def binary_search_recursive(array, target):
    '''
    This function will call `binary_search_recursive_soln` function.
    You don't need to change this function.
    
    args:
      array: a sorted array of items of the same type
      target: the element you're searching for
    '''
    return binary_search_recursive_soln(array, target, 0, len(array) - 1)


def binary_search_recursive_soln(array, target, start_index, end_index):
    '''Write a function that implements the binary search algorithm using recursion
    
    args:
      array: a sorted array of items of the same type
      target: the element you're searching for
      start_index: beginning of the index of the sub-arrays
      end_index: end of the index of the sub-arrays
         
    returns:
      int: the index of the target, if found, in the source
      -1: if the target is not found
    '''
    if start_index > end_index:  # MUST HAVE base case
        return -1
    
    mid = start_index + (end_index - start_index) // 2
    if array[mid] == target:
        return mid
    elif array[mid] < target:
        binary_search_recursive_soln(array, target, mid + 1, end_index)
    else:
        binary_search_recursive_soln(array, target, start_index, mid - 1)


def binary_search(array, target):
    '''Write a function that implements the binary search algorithm using iteration
   
    args:
      array: a sorted array of items of the same type
      target: the element you're searching for
   
    returns:
      int: the index of the target, if found, in the source
      -1: if the target is not found
    '''
    left = 0
    right = len(array)
    while left <= right:
        mid = left + (right - left) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1
