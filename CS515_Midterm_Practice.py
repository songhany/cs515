###########################################################################
# RULES: You can use the following:
# This is a paper based test
# One sheet of paper with handwritten notes on both sides (don't submit it).
# Blank paper if you find that helpful work working on your solutions  
# No other resources other than your mind.  
# 
# Name and pledge:
#
###########################################################################

###########################################################################
# Using the definition of LCS below, show the trace of function calls
# for the expression LCS("hi", "bi").  Use indentation to show which 
# calls result from previous calls.
###########################################################################

def LCS(S1, S2):
    """Length of longest common subsequence of two lists."""
    if S1 == "" or S2 == "": return 0
    elif S1[0] == S2[0]:  
        return 1 + LCS(S1[1:], S2[1:])
    else:
        return max(LCS(S1, S2[1:]), LCS(S1[1:], S2))

"""
ANSWER DONE IN CLASS:

LCS("hi", "bi")
    LCS("hi", "i")
       LCS("hi", "")
       LCS("i", "i")
           LCS("", "")
    LCS("i", "bi")
       LCS("i", "i")
           LCS("", "")
       LCS("", "bi")
"""

###########################################################################
# Here's another tracing problem:  show the function call trace
# for the call quiz(2,7).  Here's the code.
###########################################################################

def quiz(n,k):
    if k == 0: return 1
    elif k % 2 == 0:
        t = quiz(n, k//2)
        return t*t
    else: return n * quiz(n,k-1)

###########################################################################
# Write out the trace of function calls starting from fab(4,3) for the
# function defined below.
# Use indentation to indicate which calls are the result of preceding calls.
#
# Hint: You are welcome to modify the function and make it trace itself.
# But to answer the question you need to write your trace in the comment below.
###########################################################################

def fab(n,k):
    '''mystery function'''
    if n == 0 or n == 1:
        return k
    else:
        return fab(n-2,k) + fab(n-1,k)

'''
Your trace here



'''



###########################################################################
# Here's a typical question from pencil-and-paper tests.
# You should be able to read this code and figure out what it prints
# without running it in IDLE.
###########################################################################

M = ['what', 'does', 'map', 'really']
L = 2*['do'] + M 
N = [ 'map', L[3], M[2] ]  
print(N)

###########################################################################
# Here's another one like that.
###########################################################################

P = ['climate', 'youth', 'action']
Q = ['united', 'nations', 'leaders']
R = P[:2] + Q[:1] + P[2:] 
print(R)


###########################################################################
# Implement the following function.  
# It should return a list of the values of the polynomial 3x**2+3 (in words:
# three x squared plus three), applied to the first N non-negative integers.
# You may use range, map, lambda, and the exponent operator **.
# Do NOT use recursion.
###########################################################################

def poly(N):
    pass # TO-DO your code here


def testPoly():
    assert ( poly(5) == [3, 6, 15, 30, 51] )


###########################################################################
# Fill in the missing parts in the following code. 
# It should compute the same result as map(lambda x: n*x, L).
###########################################################################

def multAll(n, L):
    '''Assuming n is a number and L is a list of numbers,
       make a list by multiplying each element of L by n.
       For example, multAll(3,[3,5,7,9]) is [9,15,21,27].'''
    if L==[]:

        return None # TO-DO replace None 


    else:

        return None # TO-DO replace None 

###########################################################################
# Complete this function so it uses assert to test multAll on at 
# least the example in the docstring of multAll.
###########################################################################

def testMultAll():
    pass # TO-DO

###########################################################################
# Complete the following function, using recursion on the lists.  That means 
# you can only access L using the expressions L[0], L==[], and L[1:].  And
# the same for M.  
#
# Hint: It can be done with one recursive call, where both lists are smaller.
###########################################################################

def listProd(L,M):
    '''Assume L and M are lists of  numbers.  Return a list of their products
    at corresponding indexes.  If one list is longer than the other, include its 
    elements at the end.  See testProd for examples.'''

    pass # TO-DO 

def testProd():
    assert listProd([1,2,3], [1,2,3]) == [1, 4, 9]
    assert listProd([1,5,1], [2,3,3]) == [2,15,3]
    assert listProd([], [1,3,5,7]) == [1,3,5,7]
    assert listProd([1,2,3], [6,5,4,9,8,7]) == [6,10,12,9,8,7]

###########################################################################
# Below is an implementation of the longest common subsequence function.
# Add memoization, which will make it more efficient.  
  
# Hint: create the dictionary outside the function, so you can refer to it
# in the code you add to LCS.
###########################################################################

def LCS(S1,S2):
    '''Length of the longest common subsequence of strings S1, S2.'''
    if S1 == "" or S2 == "": 
        result = 0
    elif S1[0] == S2[0]:
        result = 1 + LCS(S1[1:], S2[1:])
    else:
        chopS1 = LCS(S1[1:], S2)
        chopS2 = LCS(S1, S2[1:])
        result = max(chopS1, chopS2)
    return result



def testLCS():
    assert LCS("sam","spam!") == 3
    assert LCS("veto", "vote") == 2
    assert LCS("tranquil", "trail") == 5




