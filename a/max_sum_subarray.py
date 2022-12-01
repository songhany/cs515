'''
The Idea:
1. We have to find the sum of "contiguous" subarray, therefore we must not change the order of array elements.
2. Let `current_sum` denotes the sum of a subarray, and `max_sum` denotes the maximum value of `current_sum`.
3. LOOP STARTS: For each element of the array, update the `current_sum` with the MAXIMUM of either:
 - The element added to the `current_sum` (denotes the addition of the element to the current subarray)
 - The element itself  (denotes the starting of a new subarray)
 - Update (overwrite) `max_sum`, if it is lower than the updated `current_sum`
4. Return `max_sum`
'''
def max_sum_subarray(arr):
    """
    :param - arr - input array
    return - number - largest sum in contiguous subarry within arr
    """
    curSum = arr[0]  # `current_sum` denotes the sum of a subarray
    maxSum = arr[0]  # `max_sum` denotes the maximum value of `current_sum` ever
    
    for num in arr[1:]:
        '''
        # Compare (current_sum + element) vs (element)
        # If (current_sum + element) is higher, it denotes the addition of the element to the current subarray
        # If (element) alone is higher, it denotes the starting of a new subarray
        '''
        curSum = max(curSum + num, num)
        maxSum = max(curSum, maxSum)
        
    return maxSum


print(max_sum_subarray([1, 2, 3, -4, 6]))
print(max_sum_subarray([1, 2, -5, -4, 1, 6]))
print(max_sum_subarray([-12, 15, -13, 14, -1, 2, 1, -5, 4]))