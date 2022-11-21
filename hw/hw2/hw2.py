'''
Created on Feb 4, 2022
@author:  Songhan Yu    10470449

CS515 - Hw 2
'''
from functools import reduce
import sys
# Be sure to submit hw2.py.    Remove the '_template' from the file name.

# Allows up to 10000 recursive calls.
# The maximum permitted limit varies from system to system.
sys.setrecursionlimit(10000)

# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

# Implement your functions here.
def ind(letter, scorelist):
    '''Find index of corresponding letter in scorelist'''
    if scorelist == []:
        return 0
    if scorelist == "":
        return 0
    if letter == scorelist[0][0]:
        return 0
    return ind(letter, scorelist[1:]) + 1

def letterScore(letter, scorelist):
    '''Input a single letter string AND a list of element, output a single number'''
    position = ind(letter, scorelist)
    return scorelist[position][1]

def wordScore(S, scorelist):
    '''Return scrabble score of that string'''
    if S == "":
        return 0
    return letterScore(S[0], scorelist) + wordScore(S[1:], scorelist)


def removeCheckedLetterFromRack(e, Rack):
    '''Removes the letter that we find from the rack. Since each letter in the Rack can only be
used once'''
    if e == Rack[0]: 
        return Rack[1:]
    else: 
        return [Rack[0]] + removeCheckedLetterFromRack(e, Rack[1:])

def isLetterOfStringInRack(S, Rack):
    '''Whether String's letter in Rack'''
    if S == '':
        return True

    if S[0] in Rack:  # if this current letter of String in Rack
        return isLetterOfStringInRack(S[1:], removeCheckedLetterFromRack(S[0], Rack))  # we check whether next letter of String in Rack or not, and we must remove current letter that has been checked from Rack
    else:
        return False

def stringInDictCanBeFormedByRack(Dict, Rack):
    '''Whether String in global Dictionary can be formed by letters in Rack. 
    If can form, we add String to list and then check next String. 
    If cannot, we directly check next String in Dictionary'''
    if Dict == []:
        return []

    if isLetterOfStringInRack(Dict[0], Rack):  # if String can be formed by letters in Rack
        return [Dict[0]] + stringInDictCanBeFormedByRack(Dict[1:], Rack)
    else:  # if cannot be formed, we directly check next String in Dictionary
        return stringInDictCanBeFormedByRack(Dict[1:], Rack)

def stringScore(strlist, scorelist):
    '''Returns an array of the word and its scrabble score'''
    if strlist == []: 
        return []
    else: 
        return [ [strlist[0], wordScore(strlist[0], scorelist)] ] + stringScore(strlist[1:], scorelist)


def scoreList(Rack):
    '''Input a Rack which is a list of lower-case letters, returns a list of all of the words in the global Dictionary with their wordScore'''
    return stringScore(stringInDictCanBeFormedByRack(Dictionary, Rack), scrabbleScores)
    
def bestWord(Rack):
    """Input a Rack, returns the highest possible scoring word from that Rack followed by its score."""
    scorelist = scoreList(Rack)
    if scorelist == []:
        return ['', 0]
    return reduce(lambda stirngWithScore1, stirngWithScore2: stirngWithScore1 if stirngWithScore1[1] > stirngWithScore2[1] else stirngWithScore2, scorelist)


# test case
if __name__ == "__main__":
    print(letterScore('c', scrabbleScores))    # 3

    print(wordScore('spam', scrabbleScores))    # 8
    print(wordScore('wow', scrabbleScores))     # 9
    print(wordScore('wow', [['o', 10], ['w', 42]]))   # 94

    print(removeCheckedLetterFromRack("a", ["a", "s", "m", "t", "p"]))   # ['s', 'm', 't', 'p']
    print(removeCheckedLetterFromRack("t", ["a", "s", "m", "t", "p"]))   # ['a', 's', 'm', 'p']

    print(isLetterOfStringInRack("spam", ["a", "s", "m", "t", "p"]))   # True
    print(isLetterOfStringInRack("wow", ['w', 'y', 'l', 'e', 'l', 'o']))   # False

    print(stringInDictCanBeFormedByRack(Dictionary, ["a", "s", "m", "t", "p"]))   # ['a', 'am', 'at', 'spam']
    
    print(scoreList(["a", "s", "m", "t", "p"]))   # [['a', 1], ['am', 4], ['at', 2], ['spam', 8]]
    print(scoreList(["a", "s", "m", "o", "f", "o"]))   # [['a', 1], ['am', 4], ['foo', 6]]

    print(bestWord(["a", "s", "m", "t", "p"]))  # ['spam', 8]