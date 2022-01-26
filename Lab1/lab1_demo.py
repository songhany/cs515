############################################################
# Name: Songhan Yu
# CS515 Lab 1
#  
############################################################

from math import factorial
from functools import reduce

def inverse(x):
    return 1.0/x

def add(x, y):
    return x + y

def e(n):
    """ e = 1/0! + 1/1! + 1/2! + 1/3! + ... + 1/n! """
    return reduce(add, map(inverse, map(factorial, list(range(n+1)))))
    




