'''
### Problem Statement

Suppose there is a staircase that you can climb in either 1 step, 2 steps, or 3 steps. In how many possible ways can you climb the staircase if the staircase has `n` steps? Write a recursive function to solve the problem.

param: n - number of steps in the staircase
Return number of possible ways in which you can climb the staircase
'''
def staircase(n):
    '''Hint'''
    # Base Case - What holds true for minimum steps possible i.e., n == 0, 1, 2 or 3? Return the number of ways the child can climb n steps.
    if n <= 0:
        return 1
    elif n == 1:
        return 1   # 1
    elif n == 2:
        return 2   # 1+1, 2
    elif n == 3:
        return 4   # 1+1+1, 1+2, 2+1, 3
    
    # Recursive Step - Split the solution into base case if n > 3.
    ways = staircase(n - 1) + staircase(n - 2) + staircase(n - 3)
    
    return ways