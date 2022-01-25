""" 
============ Function Exercise============
"""

def addTwoDigits(n):
  x = n % 10
  y = n / 10
  return x + y

def largestNumber(n):
  return 10**n - 1

def reverse(lst):
  return lst[::-1]

# print(addTwoDigits(29))

# print(largestNumber(0))
# print(largestNumber(1))
# print(largestNumber(2))

# print(reverse([1,2,3]))


""" 
============ Higher Order Functions ============
1. MAP
2. REDUCE
3. FILTER
"""

from functools import reduce


""" 
1. MAP
 """
def dbl(n):
  return 2*n

def evens(n):
  # myList = range(n)
  # doubled = map(dbl, myList)
  # return doubled
  return map(dbl, range(n))

# print(map(dbl, [1, 2, 3, 4]))

# print(evens(5))


""" 
2. REDUCE 
 """
def add(x, y):
  return x + y

# print(reduce(add, [1, 2, 3, 4]))


def span(l):
  mx = reduce(max, l)
  mn = reduce(min, l)
  return mx - mn

# print(span([3, 1, 42, 7]))
# print(span([42, 42, 42, 42]))


def summation(x, y):
  return x + y

def gauss(n):
  return reduce(summation, range(1, n+1))

def power(n):
  return n**2

def sumOfSquares(n):
  return reduce(summation, map(power, range(1, n+1)))

# print(gauss(3))  # 6
# print(gauss(10))  # 55
# print(sumOfSquares(3))  # 14
# print(sumOfSquares(10))  # 385


""" 
3. FILTER
 """
def isOdd(x):
  """returns True is x is even 
    returns False otherwise"""
  return x%2

def isEven(x):
  if x % 2 == 0:
    return True
  return False

def filterEvens(l):
  return filter(isEven, l)


# print(filter(isOdd, [1, 2, 3, 4]))
# print(filterEvens([1, 2, 3, 4]))


""" 
============ Boolean ============
"""
print(True + 41)  # 42
print(2**False == True)  # True


