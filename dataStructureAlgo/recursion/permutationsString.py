def permutations(string):
    """
    :param: input string
    Return - list of all permutations of the input string
    TODO: complete this function to return a list of all permutations of the string
    """
    if len(string) == 0:
        return ['']
    
    res = []
    dfs(list(string), 0, res)   # convert string to list
    return res

def dfs(string, curLevel, res):
    if len(string) == curLevel:
        res.append(''.join(string))  # convert string to list by ''.join(lst)
        return
    
    for i in range(curLevel, len(string)):
        swap(string, curLevel, i)
        dfs(string, curLevel + 1, res)
        swap(string, curLevel, i)
        
    return res

def swap(string, i, j):
    tmp = string[i]
    string[i] = string[j]
    string[j] = tmp

# print(permutations('ab'))
# print(permutations('abc'))
# print(permutations('abcd'))


def permutations_sol(string):
    return recursion(string, 0)

def recursion(string, index):
    output = list()

    if index >= len(string):
        return ['']


    small_output = recursion(string, index + 1)  # Recursive function call
    current_char = string[index]    # Pick a character

    # Iterate over each sub-string available in the list returned from previous call
    for subString in small_output:    
        for idx in range(0, len(small_output[0]) + 1):    # place the current character at different indices of the sub-string
            new_subString = subString[0: idx] + current_char + subString[idx:]
            output.append(new_subString)

    return output


print(permutations_sol('ab'))
print(permutations_sol('abc'))
print(permutations_sol('abcd'))
