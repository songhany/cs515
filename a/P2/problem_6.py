def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    min_val = float('inf')
    max_val = float('-inf')
    for num in ints:
        if num < min_val:
            min_val = num
        elif num > max_val:
            max_val = num
    return min_val, max_val

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")


# def get_min_max1(ints):
#     """
#     Return a tuple(min, max) out of list of unsorted integers.

#     Args:
#        ints(list): list of integers containing one or more integers
#     """
#     min_val, max_val = ints[0], ints[0]
#     for i in range(1, len(ints), 2):
#         if ints[i] < ints[i-1]:
#             if ints[i] < min_val:
#                 min_val = ints[i]
#             if ints[i-1] > max_val:
#                 max_val = ints[i-1]
#         else:
#             if ints[i-1] < min_val:
#                 min_val = ints[i-1]
#             if ints[i] > max_val:
#                 max_val = ints[i]
#     return min_val, max_val