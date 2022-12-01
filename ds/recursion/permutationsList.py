# Code
import copy

def permute(inputList):
    """
    Args: myList: list of items to be permuted
    Returns: list of permutation with each permuted item being represented by a list
    """
    if len(inputList) == 0:
        return [[]]
    
    res = []
    dfs(inputList, 0, res)
    return res

def dfs(inputList, curLevel, res):
    if len(inputList) == curLevel:
        res.append(list(inputList))
        return
        
    for i in range(curLevel, len(inputList)):
        swap(inputList, curLevel, i)
        dfs(inputList, curLevel + 1, res)
        swap(inputList, curLevel, i)
    return res

def swap(inputList, i, j):
    tmp = inputList[i]
    inputList[i] = inputList[j]
    inputList[j] = tmp


# print(permute([]))
# print(permute([0]))
# print(permute([0, 1]))
# print(permute([0, 1, 2]))


def permute1(inputList):
    finalCompoundList = []

    if len(inputList) == 0:
        finalCompoundList.append([])
    else:
        first_element = inputList[0]         # Pick one element to be permuted
        after_first = slice(1, None)         # `after_first` is an object of type 'slice' class
        rest_list = inputList[after_first]   # convert the `slice` object into a list

        # Call the recursive function to split the `rest_list` further until it meets the base condition and store the last `finalCompoundListres` output into `sub_compoundList` variable
        sub_compoundList = permute1(rest_list)

        # Once the recursion function meets the base condition, we can build the permutation by iterating through all lists of the `compoundList` returned from previous recursive call
        for aList in sub_compoundList:
            for j in range(0, len(aList) + 1):   # j refers to 'the position that can be inserted in aList'

                bList = copy.deepcopy(aList)     # A normal copy/assignment will change aList[j] element
                
                bList.insert(j, first_element)   # A new list with size +1 as compared to aList is created by inserting the `first_element` at position j in bList

                finalCompoundList.append(bList)  # Append the newly created list to the finalCompoundList

    return finalCompoundList


print(permute1([]))
print(permute1([0]))
print(permute1([0, 1]))
print(permute1([0, 1, 2]))
