
# doublelambda = lambda x : 2*x
# doublelambda(50)

# l = ["mary", "jonathan", "bob", "maria", "abi"]
# print(filter(lambda s: len(s) > 3, l))


# from math import sqrt

# def rightTrianglesCount():
#   lst = [[1, 2, 3], [3, 4, 5], [1, 1, sqrt(2)]]
#   return filter(lambda l: (l[0]**2 + l[1]**2 == l[2]**2), lst)  # this is not right

# print(rightTrianglesCount())


""" 
============ Exercise ============
"""

# def tower(n):
#   if (n == 0):
#     return 1
#   if (n == 1):
#     return 2
#   return 2**tower(n-1)

# print(tower(3))
# print(tower(4))
# print(tower(5))


def length(l):
  if l == []:
    return 0
  else:
    return 1 + length(l[1:])

def sumlist(l):
  if l == []:
    return 0
  else:
    return l[0] + sumlist(l[1:])

print(length([]))
print(length([1, 2, 3]))

print(sumlist([]))
print(sumlist([1, 2, 3]))
print(sumlist([5, 5, 5, 5]))

