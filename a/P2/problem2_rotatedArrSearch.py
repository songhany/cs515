# You can assume there are no duplicates in the array 
# and your algorithm's runtime complexity must be in the order of O(log n).
# algo: Binary Search

def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    left = 0
    right = len(input_list) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        if input_list[mid] == number:
            return mid
                                                    # l     mid     r
        elif input_list[left] <= input_list[mid]:   # 3 4 5  6  0 1 2 
            if input_list[left] <= number and number < input_list[mid]:
                right = mid - 1
            else:
                left = mid + 1
                                                       # l     mid      r
        else:  #  input_list[left] > input_list[mid]   # 5 6 0  1   2 3 4
            if input_list[mid] < number and number <= input_list[right]:    # We cannot write " if input_list[mid] > number and number >= input_list[left]: ", since this conflict with " input_list[left] > input_list[mid] ""
                left = mid + 1
            else:  # input_list[mid] >= number || number > input_list[right]:
                right = mid - 1

    return -1

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


# test case
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])