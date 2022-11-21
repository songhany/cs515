""" CS515 Homework1
Name: Songhan Yu
CWID: 10470449
"""

from functools import reduce


def mult(x, y):
  """ Returns the product of x and y """
  return x * y

def factorial(n):
  """ Input: takes a positive integer n
      Output: returns n! """
  return reduce(mult, list(range(1, n+1)))

def add(x, y):
  """ Returns the sum of x and y """
  return x + y

def mean(L):
  """ Input: takes a list
      Output: returns the mean (average) value in that list """
  return reduce(add, L) / len(L)


# test case
if __name__ == "__main__":
  print(factorial(3))
  print(factorial(4))
  print(factorial(5))
  print(mean([1, 3, 5]))
  print(mean([1, 1, 1]))
  print(mean([1, 3, 5, 7, 9]))