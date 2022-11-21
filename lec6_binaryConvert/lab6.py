from functools import reduce

def isOdd(n):
    return n % 2 == 1

def numToBinary(n):
    if n == 0:
        return ''
    elif isOdd(n):
        return numToBinary(n // 2) + "1"
    else:
        return numToBinary(n // 2) + "0"

# print(numToBinary(5))  # 101



def binaryToNum(s):
    if s == '':
        return 0
    else:
        return (ord(s[0]) - ord('0')) * 2 **(len(s)- 1) + binaryToNum(s[1:])


def binaryToNum1(s):
    if s == "":
        return 0
    else:
        if s[0] == '1':
            return binaryToNum1(s[1:]) + 2**(len(s) - 1)
        else:
            return binaryToNum1(s[1:])


def binaryToNum2(s):
    if s == "":
        return 0
    else:
        if s[-1] == '1':
            return binaryToNum2(s[:-1])*2 + 1
        else:
            return binaryToNum2(s[:-1])*2


# print(binaryToNum("1011"))  # 11
# print(binaryToNum1("1011"))  # 11 
# print(binaryToNum2("1011"))  # 11