#Name: Songhan Yu
#Pledge: I pledge my honor that I have abided by the Stevens Honor System.

from functools import reduce

def isEven(num):
    if num % 2 == 0:
        return True
    return False

def reverse_example(L):
    if L == []:
        return []
    return [L[-1]] + reverse_example(L[:-1])
    #return reverse_example(L[1:]) + L[0]

def dot(L, K):
    ''' dot([5,3], [6,4]) <-- Note that 5*6 + 3*4 = 42 '''
    if len(L) != len(K):
        return "try again"
    elif len(L) == 0 or len(K) == 0:
        return 0.0
    else:
        return L[0]*K[0] + dot(L[1:], K[1:])


def explode(S):
    """ 'spam' -> ['s', 'p', 'a', 'm'] """
    if len(S) == 0:
        return []
    return [S[0]] + explode(S[1:])


def ind(e, L):
    """ 
    ind(42, [ 55, 77, 42, 12, 42, 100 ]) -> 2
    ind(42, range(0,100)) -> 42
    ind('hi', [ 'hello', 42, True ]) -> 3  'hi' is not exit in List, return len of List
    ind('i', 'team') -> 4   'i' is not exit in String, return len of String
    """
    idx = 0
    if L == []:
        return 0
    if L == "":
        return 0
    if L[0] == e:
        return 0
    else:
        return 1 + ind(e, L[1:])


def removeAll(e,L):
    if L == []:
        return []
    if L[0] == e:
        return removeAll(e, L[1:])
    else:
        return [L[0]] + removeAll(e, L[1:])


def myFilter(f, L):
    # filter function in python
    if L == []:
        return []
    if f(L[0]):
        return [L[0]] + myFilter(f, L[1:])
    if not f(L[0]):
        return [] + myFilter(f, L[1:])


def deepReverse(L):
    # returns a deep reversal of a list
    if L == []:
        return []
    if type(L[0]) == type([]):
        return deepReverse(L[1:]) + [deepReverse(L[0])]
    else:
        return deepReverse(L[1:]) + [L[0]] 


print(dot([5,3], [6,4]))
print(explode(""))
print(explode("spam"))

print(ind(42, [ 55, 77, 42, 12, 42, 100 ]))  # 4
print(ind(42, range(0,100)))  # 42
print(ind('hi', [ 'hello', 42, True ]))  # 3
print(ind('hi', [ 'well', 'hi', 'there' ]))  # 1
print(ind('i', 'team'))  # 4
print(ind(' ', 'outer exploration'))  # 5


print(myFilter(isEven, [0, 1, 2, 3, 4, 5, 6]))


print(deepReverse([1, 2, 3]))  # [3, 2, 1]
print(deepReverse([1, [2, 3], 4]))  # [4, [3, 2], 1]
print(deepReverse([1, [2, [3, 4], [5, [6, 7], 8]]]))  # [[[8, [7, 6], 5], [4, 3], 2], 1]