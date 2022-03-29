
def fibRecursion(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibRecursion(n-1) + fibRecursion(n-2)

# print(fibRecursion(3))

''' Iterative Logic

fib  0  1  1  2  3  5
     i   
        j

    tmp = i + j
    take i to j position
    j = tmp
'''

def fibIterative(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    i = 0
    j = 1
    for index in range(n-1):
        tmp = i + j
        i = j 
        j = tmp
    return j

# print(fibIterative(3))


def fibIterative1(n):
    numPrinted = 0
    if n > 0:
        print(0)
        numPrinted += 1
        i = 0
        j = 1
        while numPrinted != n:
            print(j)
            i = j
            j = i + j
            numPrinted += 1


def printFibs(n):
    for x in range(n):
        print(fibIterative(x))
        
    for x in range(n):
        print(fibRecursion(x))

# printFibs(10)