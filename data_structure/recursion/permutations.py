import copy

def permute(inputList):
    res = []
    
    if len(inputList) == 0:
        res.append([])
    else:
        firstElement = inputList[0]
        restList = inputList[1:]
        
        subCompoundLst = permute(restList)

        for aList in subCompoundLst:
            for j in range(0, len(aList) + 1):
                bList = copy.deepcopy(aList)
                bList.insert(j, firstElement)
                res.append(bList)

    return res


def permutations(string):
    return recursion(string, 0)

def recursion(string, curIdx):
    output = list()
    
    if curIdx >= len(string):
        return ['']
    
    small_output = recursion(string, curIdx + 1)
    curChar = string[curIdx]
    
    for subString in small_output:
        for idx in range(0, len(small_output[0]) + 1):
            new_subString = subString[0: idx] + curChar + subString[idx:]
            output.append(new_subString)
            
    return output
