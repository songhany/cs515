def addTwoDigits(n):
    x = n % 10
    y = n // 10
    return x+y

def largestNumber(n):
    return 10**n - 1
def reverse(l):
    return l[::-1]




def dbl(n):
    return 2*n

def seqEvens(n):
    return list(map(dbl, range(n)))

from functools import reduce

def span(l):
    mx = reduce(max, l)
    mn = reduce(min, l)
    return mx - mn

def summation(x,y):
    return x + y
    
def gauss(n):
    return reduce(summation, range(1, n+1))

def power(n):
    return n**2

def sumOfSquares(n):
    return reduce(summation, map(power, range(1, n+1)))

def even(n):
    if n%2 == 0:
        return True
    else:
        return False

def filterEvens(l):
    return list(filter(even, l))







