def deep_reverse(arr):
    if len(arr) == 0:
        return arr
    
    deep_reversed_output = list()
    for idx in range(len(arr)-1, -1, -1):
        if type(arr[idx]) is list:
            deep_reversed_output.append(deep_reverse(arr[idx]))
        else:
            deep_reversed_output.append(arr[idx])
            
    return deep_reversed_output