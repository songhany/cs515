
def isOdd(n):
    '''Returns whether or not the integer argument is odd.'''
    return n%2 == 1

def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.'''
    if n == 0:
        return ''
    elif isOdd(n):
        return numToBinary(n//2) + "1"
    else:
        return numToBinary(n//2) + "0"

def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    if s == "":
        return 0
    else:
        if s[0] == '1':
            return binaryToNum(s[1:]) + 2**(len(s)-1)
        else:
            return binaryToNum(s[1:])
        
def binaryToNum2(s):
    if s == "":
        return 0
    else:
        if s[-1] == '1':
            return binaryToNum(s[:-1])*2 + 1
        else:
            return binaryToNum(s[:-1])*2

def binaryToNum3(s):  # binaryToNum2 another version
    if s == "":
        return 0
    else:
        return binaryToNum(s[:-1])*2 + int(s[-1])  # combine if else in binaryToNum2 to single statement


# print(binaryToNum("1011"))  # 11
# print(binaryToNum1("1011"))  # 11 
# binaryToNum1("1011")  # 11
print(binaryToNum3("1011"))  # 11

def increment(s):
    '''Precondition: s is a string of 8 bits.
    Returns the binary representation of binaryToNum(s) + 1.'''
    dec = binaryToNum(s)
    b = numToBinary(dec + 1)
    return '0'* max(0, 8 - len(b)) + b[-8:]

# print(increment('00000001'))  # 00000010
# print(increment('11111111'))  # 00000000

def count(s, n):
    '''Precondition: s is an 8-bit string and n >= 0.
    Prints s and its n successors.'''
    print(s)
    if n == 0:
        return
    else:
        x = increment(s)
        return count(x, n-1)

# print(count("00000000", 4))
# print(count("11111110", 5))


def numToTernary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the ternary representation of non-negative integer
    n. If n is 0, the empty string is returned.'''
    if n == 0:
        return ''
    elif n%3 == 1:
        return numToTernary(n//3) + "1"
    elif n%3 == 2:
        return numToTernary(n//3) + "2"
    elif n%3 == 0:
        return numToTernary(n//3) + "0"


def ternaryToNum(s):
    '''Precondition: s is a string of 0s, 1s, and 2s.
    Returns the integer corresponding to the ternary representation in s.
    Note: the empty string represents 0.'''
    if s == "":
        return 0
    else:
        return ternaryToNum(s[:-1])*3 + int(s[-1])


# print(numToTernary(42))  # 1120
# print(numToTernary(4242))  # 12211010

# print(ternaryToNum('1120'))  # 42
# print(ternaryToNum('12211010'))  # 4242
