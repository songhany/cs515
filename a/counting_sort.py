def counting_sort(arr):
    # Find the maximum element in the array
    max_element = max(arr)
    
    # Initialize the count array with all zeros
    count = [0] * (max_element + 1)
    
    # Count the frequency of each element in the array
    for x in arr:
        count[x] += 1
    
    # Reconstruct the sorted array
    sorted_arr = []
    for i in range(len(count)):
        for j in range(count[i]):
            sorted_arr.append(i)
    
    return sorted_arr


def counting_sort(arr):
    # Find the maximum element in the array
    max_element = max(arr)
    
    # Initialize the count array with all zeros
    count = [0] * (max_element + 1)
    
    # Count the frequency of each element in the array
    for x in arr:
        count[x] += 1
    
    # Reconstruct the sorted array
    sorted_arr = []
    for i in range(len(count)):
        for j in range(count[i]):
            sorted_arr.append(i)
    
    return sorted_arr


def max_sum(arr):
    # step 1
    counts = {}
    for x in arr:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1
    
    # step 2
    sorted_arr = counting_sort(arr)[::-1]
    
    # step 3
    num1 = []
    num2 = []
    
    # step 4
    for x in sorted_arr:
        if len(num1) <= len(num2):
            num1.append(str(x))
        else:
            num2.append(str(x))
    
    # step 5
    return [int(''.join(num1)), int(''.join(num2))]


def max_sum(arr):
    # step 1
    counts = {}
    for x in arr:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1
    
    # step 2
    sorted_arr = []
    for i in range(9, -1, -1):
        if i in counts:
            sorted_arr.extend([i] * counts[i])
    
    # step 3
    num1 = []
    num2 = []
    
    # step 4
    for x in sorted_arr:
        if len(num1) <= len(num2):
            num1.append(str(x))
        else:
            num2.append(str(x))
    
    # step 5
    return [int(''.join(num1)), int(''.join(num2))]