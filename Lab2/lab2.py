#Name: Songhan Yu
#Pledge: I pledge my honor that I have abided by the Stevens Honor System.

from functools import reduce

def reverse_example(L):
    if L == []:
        return []
    return [L[-1]] + reverse_example(L[:-1])
    #return reverse_example(L[1:]) + L[0]

def dot(L, K):
    '''Input: list
        Output: sum of the products of the elements '''
    if len(L) != len(K):
        return "try again"
    elif len(L) == 0 or len(K) == 0:
        return 0.0
    else:
        return L[0]*K[0] + dot(L[1:], K[1:])


def explode(S):
    if len(S) == 0:
        return []
    return    [S[0]] + explode(S[1:])


def ind(e,L):
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


def myFilter(f,L):
    pass


def deepReverse(L):
    pass

print(dot([5,3], [6,4]))
print(explode(""))
print(explode("spam"))

print(ind(42, [ 55, 77, 42, 12, 42, 100 ]))  # 4
print(ind(42, range(0,100)))  # 42
print(ind('hi', [ 'hello', 42, True ]))  # 3
print(ind('hi', [ 'well', 'hi', 'there' ]))  # 1
print(ind('i', 'team'))  # 4
print(ind(' ', 'outer exploration'))  # 5