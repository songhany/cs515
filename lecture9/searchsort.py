'''
CS 115 - Sequential search, binary search
'''
import random
import time

def sequential_search(lst, key):
    '''Searches the list for the key. If the key is present, the function
    returns the index of the key. Otherwise, it returns -1.'''
    for i in range(len(lst)):
        if lst[i] == key:
            return i
    return -1



def binary_search(lst, key):
    '''Searches the list for the key. If the key is present, the function
    returns the index of the key. Otherwise, it returns -1.
    NOTE: binary search works only if the list is sorted.'''
    low = 0
    high = len(lst) - 1
    while low <= high:
        mid = low + (high - low) // 2 # (low+high)//2
        if lst[mid] == key:
            return mid
        if lst[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def bs_trace(lst, key):
    '''Searches the list for the key. If the key is present, the function
    returns the index of the key. Otherwise, it returns -1.
    NOTE: binary search works only if the list is sorted.'''
    low = 0
    high = len(lst) - 1
    iteration = 0
    print("iter", "low", "high", "mid", sep = "\t|\t")
    print("-"*55)
    while low <= high:
        mid = low + (high - low) // 2
        print(str(iteration), str(low), str(high), str(mid), sep = "\t|\t")
        iteration += 1
        if lst[mid] == key:
            return mid
        if lst[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1

#### Testing ####
lst = [5, 9, -2, -12, 7]
key = -121
index = sequential_search(lst, key)
if index >= 0:
    print('Key %d found at index %d.' % (key, index))
else:
    print('Key %d not found.' % key)

lst = [1, 3, 5, 7, 9, 10, 11]
key = 3
index = binary_search(lst, key)
if index >= 0:
    print('Key %d found at index %d.' % (key, index))
else:
    print('Key %d not found, but can be inserted at index %d.' % (key, -index - 1))
    
### Speed Comparison ###
print("Searching over a list with 1M elements ... ")
lst = [random.randint(1, 1000) for _ in range(50000000)]
lst.sort()

start = time.time()
sequential_search(lst, 200)
elapsed = (time.time() - start) * 1000
print('Sequential search: %0.3f ms' % elapsed)

start = time.time()
binary_search(lst, 200)
elapsed = (time.time() - start) * 1000
print('Binary search:     %0.3f ms' % elapsed)

######## CHALLENGE ###########
## Problem Statement: Given a sorted array with possible duplicate elements.
## Find number of occurrences of input ‘key’ in log N time.
##########



