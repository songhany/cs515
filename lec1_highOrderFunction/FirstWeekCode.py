def dbl(n):
    return 2*n

def quad(n):
    return dbl(dbl(n))
def add(x,y):
    return x + y

#1. Solve the circle area problem
def area(r):
    """ Input: r is positive integer
        Output: circumference of the circle with radius r """
    pi_val = 3.1415
    return pi_val*r**2

#2. Show how to use math library
from math import pi
print(pi)

from math import *
import math
print(math.pi)

from math import pi, sqrt
print(sqrt(25))

print(dir(math)) #prints list of functions found in math library

def area(r):
    return 2*pi*r

#Strings: any sequence of characters within quotation marks

name1 = "John"
name2 = "Eva"
#find length of a string
len(name1)
len("Hakuna Matata")

#Indexing: Find the symbol that is located at any given position or index
#The first symbol has index zero
print(name2[0])
print(name2[1])
print(name2[2])
#name2[3]#error
#Negative indexing
print(name2[-1])

#slicing: find parts of a string
bestFood = "pizza margherita"
bestFood[0:3]
bestFood[1:]
bestFood[:5]
bestFood[1:-1]

#String arithmetics
'fri'+'day'
'friday'*3

#List: "package" a bunch of objects(numbers, string) together
numbers = [4, 5, 7, 0, 3]
names = ['john', 'eva','mary', 'logan']

combination1 = [4, 'john', 3, 'river']
combination2 = [4, 'john', [5, 6, 7]]
list_func = [dbl, quad]
list_func[0](9)
list_exp = [1+3, 4+9]
#list length
print(len(numbers))
#indexing
print(numbers[4])
#slicing
print(numbers[2:4])
#list arithmetic
print([1, 3, 5] + [2, 4, 6])
print(['hello world']*5)
#update list elements
numbers[0] = 'four'

# Range() objects that create sequences of number
print(list(range(1, 11)))
print(list(range(1, 11, 2)))

#Mapping with python (TRY THIS)
map(dbl, [0, 1, 2, 3, 4])

#reduce function (TRY THIS)
from functools import reduce
reduce(add, [1, 2, 3, 4])

