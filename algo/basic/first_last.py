def first_and_last_index(arr, number):
    firstIdx = find_start_index(arr, number, 0, len(arr) - 1)
    lastIdx = find_end_index(arr, number, 0, len(arr) - 1)
    return [firstIdx, lastIdx]

def find_start_index(arr, number, startIdx, endIdx):
    if startIdx > endIdx:
        return -1
    
    midIdx = startIdx + (endIdx - startIdx) // 2
    if arr[midIdx] == number:
        current_start_pos = find_start_index(arr, number, startIdx, midIdx - 1)
        if current_start_pos != -1:
            start_pos = current_start_pos
        else:
            start_pos = midIdx
        return start_pos
    
    elif arr[midIdx] < number:
        return find_start_index(arr, number, midIdx + 1, endIdx)
    else:
        return find_start_index(arr, number, startIdx, midIdx - 1)
        
def find_end_index(arr, number, startIdx, endIdx):
    if startIdx > endIdx:
        return -1
    
    midIdx = startIdx + (endIdx - startIdx) // 2
    if arr[midIdx] == number:
        current_end_pos = find_end_index(arr, number, midIdx + 1, endIdx)
        if current_end_pos != -1:
            end_pos = current_end_pos
        else:
            end_pos = midIdx
        return end_pos
    
    elif arr[midIdx] < number:
        return find_end_index(arr, number, midIdx + 1, endIdx)
    else:
        return find_end_index(arr, number, startIdx, midIdx - 1)


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    solution = test_case[2]
    output = first_and_last_index(input_list, number)
    if output == solution:
        print("Pass")
    else:
        print("Fail")

input_list = [0, 1, 2, 3, 3, 3, 3, 4, 5, 6]
number = 3
solution = [3, 6]
test_case_2 = [input_list, number, solution]
test_function(test_case_2)