'''
Created on March 28, 2022
@author:   Songhan Yu  10470449
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.

CS515 - Hw 6
'''
# Number of bits for data in the run-length encoding format.
# The assignment refers to this as k.
COMPRESSED_BLOCK_SIZE = 5

# Number of bits for data in the original format.
MAX_RUN_LENGTH = 2 ** COMPRESSED_BLOCK_SIZE - 1

# Do not change the variables above.
# Write your functions here. You may use those variables in your code.

def cnt(S, num, maxRunLength):
    '''count number of similar string'''
    if S == '':
        return 0
    elif maxRunLength == 0:
        return 0
    elif int(S[0]) == num:
        return cnt(S[1:], num, maxRunLength - 1) + 1
    return 0

def numToBinaryStringWithPadZero(num, compressedBlockSize):
    '''Convert a number into a binary string'''
    binary = numToBinary(num)
    if len(binary) <= compressedBlockSize:
        return '0' * (compressedBlockSize - len(binary)) + binary

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
    if s == '':
        return 0
    else:
        return (ord(s[0]) - ord('0')) * 2 **(len(s)- 1) + binaryToNum(s[1:])
    

def compress(S):
    '''takes a binary string S of length 64 AND return a run-length encoding of input string'''
    if S == '':
        return ''
    else:
        num = cnt(S, 0, MAX_RUN_LENGTH)
        c = compressHelper(S[num:], 1)
        return numToBinaryStringWithPadZero(num, COMPRESSED_BLOCK_SIZE) + c[0] + compress(S[(num+c[1]):])

def compressHelper(S, n):
    '''takes a binary string S of length 64'''
    if S == '':
        return ['', 0]
    num = cnt(S, n, MAX_RUN_LENGTH)
    return [numToBinaryStringWithPadZero(num, COMPRESSED_BLOCK_SIZE), num]


def uncompress(C):
    '''undo the compress'''
    if C == '':
        return ''
    return '0' * binaryToNum(C[0: COMPRESSED_BLOCK_SIZE]) + '1' * binaryToNum(C[COMPRESSED_BLOCK_SIZE:(2*COMPRESSED_BLOCK_SIZE)]) + uncompress(C[(2*COMPRESSED_BLOCK_SIZE):])

def compression(S):
    '''return the ratio of the compressed size to the original size for image S'''
    return len(compress(S))/(len(S))


'''Professor I.Lai is wrong 
since there are possible that encoded string will become longer than the initial sstring. 
His algorithm will always have exception cases that make encoded string could probably longer than the initial one.'''


# test case
if __name__ == "__main__":
    sequence = '0' * 64
    print(compress(sequence))  # '1111100000111110000000010'
    print(uncompress(compress(sequence)))
    print(compression(sequence))

    Penguin = "00011000"+"00111100"*3 + "01111110"+"11111111"+"00111100"+"00100100"
    Smile = "0"*8 + "01100110"*2 + "0"*8 + "00001000" + "01000010" + "01111110" + "0"*8
    Five = "1"*9 + "0"*7 + "10000000"*2 + "1"*7 + "0" + "00000001"*2 + "1"*7 + "0"

    # print(compress(Penguin))
    # print(uncompress(compress(Penguin)))
    # print(compression(Penguin))

    # print(compress(Smile))
    # print(uncompress(compress(Smile)))
    # print(compression(Smile))

    # print(compress(Five))
    # print(uncompress(compress(Five)))
    # print(compression(Five))