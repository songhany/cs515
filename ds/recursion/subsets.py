def subsets(arr):
    """
    :param: arr - input integer array
    Return - list of lists (two dimensional array) where each list represents a subset
    TODO: complete this method to return subsets of an array
    """
    res = list()
    path = list()
    dfs(arr, 0, path, res)
    return res

def dfs(arr, curLevel, path, res):
    if len(arr) == curLevel:
        res.append(list(path))
        return
    
    path.append(arr[curLevel])
    dfs(arr, curLevel + 1, path, res)
    path.pop(len(path) - 1)
    
    dfs(arr, curLevel + 1, path, res)



def subsets_sol(arr):
    return recursion(arr, 0)

def recursion(arr, curIdx):
    if curIdx >= len(arr):
        return [[]]

    sub_output = recursion(arr, curIdx + 1)

    output = list()
    for element in sub_output:   # append existing subsets
        output.append(element)

    for element in sub_output:   # add current elements to existing subsets and add them to the output
        current = list()
        current.append(arr[curIdx])
        current.extend(element)
        output.append(current)

    return output


print(subsets_sol([9]))
print(subsets_sol([5, 7]))
print(subsets_sol([9, 12, 15]))
print(subsets_sol([9, 8, 9, 8]))
