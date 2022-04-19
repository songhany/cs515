'''
                            change(4, [1, 5, 10])
                            /use             \ lose

'''
import sys
sys.setrecursionlimit(10000)

def change(amount, coins):
    if amount == 0:
        return 0
    elif coins == []:
        return float('inf')
    elif coins[0] > amount:
        return change(amount, coins[1:])
    else:
        useIt = 1 + change(amount - coins[0], coins)    # don't skip the first coin, because I can reuse it
        
        loseIt = change(amount, coins[1:])
        return min(useIt, loseIt)

print(change(48, [1, 5, 10, 25, 50]))
print(change(48, [1, 7, 24, 42]))
print(change(35, [1, 3, 16, 30, 50]))
print(change(8, [1, 4, 6]))