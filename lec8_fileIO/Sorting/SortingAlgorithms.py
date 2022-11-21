##############
#Selection Sort O(n**2)
##############
def selectionSort(listToSort):
    for curr_index in range(len(listToSort)):
        minIndex = indexOfMin(listToSort, curr_index)
        swap(listToSort, curr_index, minIndex)
            

def indexOfMin(aList, startIndex):
    minIndex = startIndex
    for i in range(startIndex, len(aList)):
        if aList[i] < aList[minIndex]:
            minIndex = i
    return minIndex

def swap(aList, i, j):
    aList[i],aList[j] = aList[j], aList[i]

#############################
#Quick Sort O(nlogn)
#############################

def partition(l, start, end):
    pivot = l[start]
    i = start + 1
    j = end
    while True:
        while i<=j and l[i] <= pivot:
            i += 1
        while i<=j and l[j] >= pivot:
            j -= 1
        if i <= j:
            swap(l, i, j)
        else:
            break
    swap(l, start, j)
    return j

def quick_sort(l, start, end):
    if start >= end:
        return
    p = partition(array, start, end)
    quick_sort(l, start, p - 1)
    quick_sort(l, p + 1, end)
    
array = [29,99,27,41,66,28,44,78,87,19,31,76,58,88,83,97,12,21,44]
quick_sort(array, 0, len(array) - 1)
print(array)
            
