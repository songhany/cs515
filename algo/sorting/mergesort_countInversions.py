# application of merge sort
def count_inversions(arr):
    start_index = 0
    end_index = len(arr) - 1
    output = inversion_count_func(arr, start_index, end_index)
    return output


def inversion_count_func(arr, start_index, end_index):
    if start_index >= end_index:
        return 0

    mid_index = start_index + (end_index - start_index) // 2
    
    left_answer = inversion_count_func(arr, start_index, mid_index)  # find number of inversions in left-half
    right_answer = inversion_count_func(arr, mid_index + 1, end_index)  # find number of inversions in right-half
    output = left_answer + right_answer
    
    # merge two sorted halves and count inversions while merging
    output += merge_two_sorted_halves(arr, start_index, mid_index, mid_index + 1, end_index)
    return output


def merge_two_sorted_halves(arr, start_one, end_one, start_two, end_two):
    count = 0
    leftIdx = start_one
    rightIdx = start_two
    outputLength = (end_two - start_two + 1) + (end_one - start_one + 1)
    outputList = [0 for _ in range(outputLength)]
    idx = 0

    while idx < outputLength:  # idx is valid
        if arr[leftIdx] <= arr[rightIdx]:    # if left <= right, it's not an inversion
            outputList[idx] = arr[leftIdx]
            leftIdx += 1
        else:
            count = count + (end_one - leftIdx + 1)           # left > right hence it's an inversion
            outputList[idx] = arr[rightIdx]
            rightIdx += 1
        idx = idx + 1


        if leftIdx > end_one:
            for i in range(rightIdx, end_two + 1):
                outputList[idx] = arr[i]
                idx += 1
            break

        elif rightIdx > end_two:
            for i in range(leftIdx, end_one + 1):
                outputList[idx] = arr[i]
                idx += 1
            break

    idx = start_one
    for i in range(outputLength):
        arr[idx] = outputList[i]
        idx += 1
        
    return count


def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]
    if count_inversions(arr) == solution:
        print("Pass")
    else:
        print("Fail")


arr = [54, 99, 49, 22, 37, 18, 22, 90, 86, 33]
solution = 26
test_case = [arr, solution]
test_function(test_case)


arr = [1, 2, 4, 2, 3, 11, 22, 99, 108, 389]
solution = 2
test_case = [arr, solution]
test_function(test_case)