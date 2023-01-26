'''
Rearrange Array Elements so as to form two number such that their sum is maximum. Return these two numbers. 
1. You can assume that all array elements are in the range [0, 9]. 
2. The number of digits in both the numbers cannot differ by more than 1. 
3. You're not allowed to use any sorting function that Python provides 
4. and the expected time complexity is O(nlog(n)).

for e.g. [1, 2, 3, 4, 5]

The expected answer would be [531, 42]. Another expected answer can be [542, 31]. In scenarios such as these when there are more than one possible answers, return any one.
'''

def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    # step 1
    counts = {}
    for x in input_list:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1
    
    # step 2
    sorted_arr = []
    for i in range(9, -1, -1):
        if i in counts:
            tmp = [i] * counts[i]
            sorted_arr.extend(tmp)
    
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

def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")



# test case
test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
test_function([[0, 9, 3, 6, 4], [940, 63]])

test_function([[0, 0], [0, 0]])



# def rearrange_digits1(input_list):  # O(n^2)
#     """
#     Rearrange Array Elements so as to form two number such that their sum is maximum.

#     Args:
#        input_list(list): Input List
#     Returns:
#        (int),(int): Two maximum sums
#     """
#     # create an auxiliary array to count the number of occurrences of each digit
#     count = [0] * 10
#     for i in input_list:
#         count[i] += 1
    
#     # initialize the two numbers as empty strings
#     num1 = ""
#     num2 = ""
    
#     # use a flag to alternate between adding digits to num1 and num2
#     flag = True
    
#     # iterate through the count array in reverse order
#     for i in range(9, -1, -1):
#         # add the appropriate number of digits to num1 and num2
#         for j in range(count[i]):
#             if flag:
#                 num1 += str(i)
#             else:
#                 num2 += str(i)
#             flag = not flag

#     # return the two numbers as integers
#     return int(num1), int(num2)